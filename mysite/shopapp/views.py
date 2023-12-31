"""
В этом модуле лежат различные наборы представлений.

Разные view интернет-магазина: по товарам, заказам и т.д.
"""
import logging
from csv import DictWriter
from timeit import default_timer

from django.contrib.syndication.views import Feed
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group, User
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from drf_spectacular.utils import extend_schema

from .common import save_csv_products
from .forms import ProductForm, OrderForm, GroupForm
from .models import Product, Order, ProductImage
from .serializers import ProductSerializer, OrderSerializer


log = logging.getLogger(__name__)


class LatestProductsFeed(Feed):
    title = "Latest Products"
    llink = reverse_lazy("shopapp:product_details")
    description = "Updates on the latest products"

    def items(self):
        return Product.objects.order_by('-created_ad')[:10]

    def item_title(self, item: Product):
        return item.name

    def item_description(self, item: Product):
        return item.description[:200]

@extend_schema(description="Product views CRUD")
class ProductViewSet(ModelViewSet):
    """
    Набор представлений для действий над Product
    Полный CRUD для сущностей товара
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    search_fields = ["name", "description"]
    filterset_fields = [
        "name",
        "description",
        "price",
        "discount",
        "archived",
    ]
    ordering_fields = [
        "name",
        "price",
        "discount",
    ]
    @method_decorator(cache_page(60 * 2))
    def list(self, *args, **kwargs):
        # print("hello products list")
        return super().list(*args, **kwargs)
    @action(methods=["get"], detail=False)
    def download_csv(self, request: Request):
        response = HttpResponse(content_type="text/csv")
        filename = "products_export.csv"
        response["Content-Disposition"] = f"attachment: filename={filename}"
        queryset = self.filter_queryset(self.get_queryset())
        fields = [
            "name",
            "description",
            "price",
            "discount",
        ]
        queryset = queryset.only(*fields)
        writer = DictWriter(response, fieldnames=fields)
        writer.writeheader()

        for product in queryset:
            writer.writerow({
                field: getattr(product, field)
                for field in fields
            })
        return response
    @action(
        detail=False,
        methods=["post"],
        parser_classes=[MultiPartParser]
    )
    def upload_csv(self, request: Request):
        products = save_csv_products(
            request.FILES["file"].file,
            encoding=request.encoding,
        )
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filterset_fields = [
        "delivery_address",
        "promocode",
        "user",
    ]
    ordering_fields = [
        "created_ad",
    ]

class ShopIndexView(View):
    # @method_decorator(cache_page(60 * 2))
    def get(self, request: HttpRequest) -> HttpResponse:
        products = [
            ('Laptop', 1999),
            ('Desktop', 2999),
            ('Smartphone', 999),
        ]
        context ={
            "time_running": default_timer(),
            "products": products,
            "items": 1,
        }
        print("shop index context", context)
        log.debug("Products for shop index: %s", products)
        log.info("Rendering shop index")
        return render(request, 'shopapp/shop-index.html', context=context)

class GroupListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": GroupForm(),
            "groups": Group.objects.prefetch_related('permissions').all(),
        }
        return render(request, 'shopapp/groups-list.html', context=context)

    def post(self, request: HttpRequest):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.path)

class ProductDetailsView(DetailView):
    template_name = 'shopapp/products-details.html'
    # model = Product
    queryset = Product.objects.prefetch_related("images")
    context_object_name = "product"

class ProductsListView(ListView):
    template_name = 'shopapp/products-list.html'
    # model = Product
    context_object_name = "products"
    queryset = Product.objects.filter(archived=False)

class ProductCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.has_perm("shopapp.add_product")
    model = Product
    # fields = "name", "price", "description", "discount", "preview"
    form_class = ProductForm
    success_url = reverse_lazy("shopapp:products_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ProductUpdateView(UserPassesTestMixin, UpdateView):

    model = Product
    # fields = "name", "price", "description", "discount", "preview"
    form_class = ProductForm
    template_name_suffix = "_update_form"

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        return (
                user.is_superuser or
                (product.created_by == user or user.has_perm("shopapp.change_product"))
        )

    def get_success_url(self):
        return reverse(
            "shopapp:product_details",
            kwargs={"pk": self.object.pk},
        )

    def form_valid(self, form):
        response = super().form_valid(form)
        for image in form.files.getlist("images"):
            ProductImage.objects.create(
                product=self.object,
                image=image,
            )
        return response

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("shopapp:products_list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)

class OrdersListView(LoginRequiredMixin, ListView):
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("products")
        .all()
    )

class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "shopapp.view_order"
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("products")
    )

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("shopapp:orders_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        log.info("Оформление заказа: %s", self.object.pk)
        return response

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            "shopapp:order_details",
            kwargs={"pk": self.object.pk},
        )
class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy("shopapp:orders_list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

class ProductsDataExportView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        products = Product.objects.order_by("pk").all()
        products_data = [
            {
                "pk": product.pk,
                "name": product.name,
                "price": product.price,
                "archived": product.archived,
            }
            for product in products
        ]
        elem = products_data[0]
        name = elem["name"]
        print("name:", name)
        return JsonResponse({"products": products_data})

class OrdersDataExportView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        orders = Order.objects.all()
        orders_data = [
            {
                "id": order.id,
                "delivery_address": order.delivery_address,
                "promocode": order.promocode,
                "user_id": order.user_id,
                "product_ids": list(order.products.values_list('id', flat=True))
            }
            for order in orders
        ]
        return JsonResponse({"orders": orders_data})

class UserOrdersListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'shopapp/user_orders_list.html'
    context_object_name = 'orders'
    paginate_by = 10

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        self.owner = user
        return Order.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = self.owner
        return context

    def get_success_url(self):
        return reverse_lazy('user_orders', kwargs={'user_id': self.owner.id})

def export_user_orders(request, user_id):
    user = get_object_or_404(User, id=user_id)
    cache_key = f"user_orders_export_{user_id}"
    cached_data = cache.get(cache_key)

    if cached_data:
        return JsonResponse(cached_data)

    orders = Order.objects.filter(user=user).order_by('pk')
    serializer = OrderSerializer(orders, many=True)
    serialized_data = serializer.data

    cache.set(cache_key, serialized_data)

    return JsonResponse(serialized_data, safe=False)