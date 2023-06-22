from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from .models import Article

class ArticlesListView(ListView):
    model = Article
    template_name = 'blogapp/article_list.html'
    queryset = (
        Article.objects
        .filter(pub_date__isnull=False)
        .order_by("-pub_date")
    )

class ArticlesDetailView(DetailView):
    model = Article

class LatestArticlesFeed(Feed):
    title = "Blog articles (latest)"
    description = "Updates on changes and addition blog articles"
    link = reverse_lazy("blogapp:articles")

    def items(self):
        return (
            Article.objects
            .filter(pub_date__isnull=False)
            .order_by("-pub_date")[:5]
        )

    def item_title(self, item: Article):
        return item.title

    def item_description(self, item: Article):
        return item.content[:200]



