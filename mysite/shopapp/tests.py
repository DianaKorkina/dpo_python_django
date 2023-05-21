from string import ascii_letters
from random import choices

from django.contrib.auth.models import User, Permission
from django.test import TestCase
from django.urls import reverse

from mysite import settings
from .models import Product, Order
from shopapp.utils import add_two_numbers


class AddTwoNumbersTestCase(TestCase):
    def test_add_two_numbers(self):
        result = add_two_numbers(2, 3)
        self.assertEquals(result, 5)

class ProductCreateViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_superuser('username', 'Pas$w0rd')

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)
        self.product_name = "".join(choices(ascii_letters, k=10))
        Product.objects.filter(name=self.product_name).delete()
    def test_create_product(self):
        response = self.client.post(
            reverse("shopapp:product_create"),
            {
                "name": self.product_name,
                "price": "123.34",
                "description": "A good table",
                "discount": "10",
            }, HTTP_USER_AGENT='Mozilla/5.0'
        )
        self.assertEquals(response.status_code, 302)
        self.assertTrue(
            Product.objects.filter(name=self.product_name).exists()
        )

class ProductDetailsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        user = User.objects.create_user(username="testuser", password="testpassword")
        cls.product = Product.objects.create(name="Best Product", created_by=user)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.product.delete()


    def test_get_product(self):
        response = self.client.get(
            reverse("shopapp:product_details", kwargs={"pk": self.product.pk}),
            HTTP_USER_AGENT='Mozilla/5.0'
        )
        self.assertEqual(response.status_code, 200)

    def test_get_product_end_check_content(self):
        response = self.client.get(
            reverse("shopapp:product_details", kwargs={"pk": self.product.pk}),
            HTTP_USER_AGENT='Mozilla/5.0'
        )
        self.assertContains(response, self.product.name)

class ProductsListViewTestCase(TestCase):
    fixtures = [
        'users-fixture.json',
        'products-fixture.json',
    ]

    def test_products(self):
        expected_products = Product.objects.filter(archived=False).all()

        response = self.client.get(reverse("shopapp:products_list"), HTTP_USER_AGENT='Mozilla/5.0')

        self.assertQuerysetEqual(
            response.context["products"],
            expected_products,
            transform=lambda p: p,
            ordered=False
        )

        self.assertTemplateUsed(response, 'shopapp/products-list.html')

class OrdersListViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username="bob_test", password="Pas$w0rd")
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_orders_view(self):
        response = self.client.get(reverse("shopapp:orders_list"), HTTP_USER_AGENT='Mozilla/5.0')
        self.assertContains(response, "Orders")

    def test_orders_view_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse("shopapp:orders_list"), HTTP_USER_AGENT='Mozilla/5.0')
        self.assertEqual(response.status_code, 302)
        self.assertIn(str(settings.LOGIN_URL), response.url)

class ProductsExportViewTestCase(TestCase):
    fixtures = [
        'users-fixture.json',
        'products-fixture.json',
        'orders-fixture.json',
    ]

    def test_get_products_view(self):
        response = self.client.get(reverse("shopapp:products-export"), HTTP_USER_AGENT='Mozilla/5.0')
        self.assertEqual(response.status_code, 200)
        products = Product.objects.order_by("pk").all()
        expected_data = [
            {
                "pk": product.pk,
                "name": product.name,
                "price": product.price,
                "archived": product.archived,
            }
            for product in products
        ]
        products_data = response.json()
        self.assertEqual(
            products_data["products"],
            expected_data,
        )


class OrderDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        permission = Permission.objects.get(codename='view_order')
        cls.user.user_permissions.add(permission)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.user.delete()

    def setUp(self):
        self.client.force_login(self.user)
        self.order = Order.objects.create(user=self.user, delivery_address='Test Address', promocode='TESTCODE')

    def tearDown(self):
        self.order.delete()

    def test_order_details(self):
        response = self.client.get(
            reverse('shopapp:order_details', kwargs={'pk': self.order.pk}),
            HTTP_USER_AGENT='Mozilla/5.0')

        self.assertContains(response, self.order.delivery_address)
        self.assertContains(response, self.order.promocode)
        self.assertEqual(response.context['order'], self.order)

class OrdersExportViewTestCase(TestCase):
    fixtures = [
        'users-fixture.json',
        'products-fixture.json',
        'orders-fixture.json',
    ]
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        permission = Permission.objects.get(codename='view_order')
        cls.user.user_permissions.add(permission)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.user.delete()

    def setUp(self):
        self.client.force_login(self.user)

    def test_get_orders_view(self):
        response = self.client.get(reverse("shopapp:orders-export"), HTTP_USER_AGENT='Mozilla/5.0')
        self.assertEqual(response.status_code, 200)
        orders = Order.objects.all()
        expected_data = [
            {
                "id": order.id,
                "delivery_address": order.delivery_address,
                "promocode": order.promocode,
                "user_id": order.user_id,
                "product_ids": list(order.products.values_list('id', flat=True))
            }
            for order in orders
        ]
        orders_data = response.json()
        self.assertEqual(
            orders_data["orders"],
            expected_data,
        )