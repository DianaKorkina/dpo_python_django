from django.contrib.auth.models import User

from django.core.management import BaseCommand
from django.db.models import Avg, Max, Min, Count, Sum

from shopapp.models import Product, Order

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Start demo aggregate")

        orders = Order.objects.annotate(
            total=Sum("products__price"),
            products_count=Count("products"),
        )
        for order in orders:
            print(
                f"Order #{order.id}"
                f"with {order.products_count} "
                f"products worth {order.total}"
            )
        # result = Product.objects.aggregate(
        #     Avg("price"),
        #     Min("price"),
        #     Max("price"),
        #     Count("id"),
        # )
        # print(result)
        self.stdout.write("Done")