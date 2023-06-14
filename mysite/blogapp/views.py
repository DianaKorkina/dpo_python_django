from django.views.generic import ListView
from .models import Article

class ArticlesListView(ListView):
    model = Article
    template_name = 'blogapp/article_list.html'
    queryset = Article.objects.select_related('author', 'category').prefetch_related('tags').defer('content')
