from django.urls import path
from .views import (
    ShopIndexView,
    GroupListView,
    ProductDetailsView,
    ProductsListView,
    ProductCreateView,
    OrdersListView,
    OrderDetailView,
    ProductUpdateView,
    ProductDeleteView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView
)


app_name = "shopapp"
urlpatterns = [
    path("", ShopIndexView.as_view(), name="index"),
    path("groups/", GroupListView.as_view(), name="groups_list"),
    path("products/", ProductsListView.as_view(), name="products_list"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>", ProductDetailsView.as_view(), name="product_details"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/archive/", ProductDeleteView.as_view(), name="product_delete"),
    path("orders/", OrdersListView.as_view(), name="orders_list"),
    path("orders/<int:pk>", OrderDetailView.as_view(), name="order_details"),
    path("orders/create/", OrderCreateView.as_view(), name="order_create"),
    path("orders/<int:pk>/update/", OrderUpdateView.as_view(), name="order_update"),
    path("products/<int:pk>/delete/", OrderDeleteView.as_view(), name="order_delete"),
]