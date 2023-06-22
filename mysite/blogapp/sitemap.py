from django.contrib.sitemaps import Sitemap

from blogapp.models import Article


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    def items(self):
        return (
            Article.objects
            .filter(pub_date__isnull=False)
            .order_by("-pub_date")[:5]
        )