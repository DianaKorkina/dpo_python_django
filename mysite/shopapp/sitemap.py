from django.contrib.sitemaps import Sitemap

from shopapp.models import Product


class ShopSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Product.objects.all()

