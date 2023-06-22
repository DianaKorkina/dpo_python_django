from django.urls import path, include
from .views import (
    ArticlesListView,
    ArticlesDetailView,
    LatestArticlesFeed,
)

app_name = "blogapp"

urlpatterns = [
    path("articles/", ArticlesListView.as_view(), name="articles"),
    path("articles/<int:pk>/", ArticlesDetailView.as_view(), name="article"),
    path("articles/latest/feed/", LatestArticlesFeed(), name="articles-feed"),
]
