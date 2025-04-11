from django.urls import path

from .views import (
    AritcleUpdateView,
    ArticleCreateView,
    ArticleDeleteView,
    ArticleListView,
)

urlpatterns = [
    path("", ArticleListView.as_view(), name="home"),
    path("create/", ArticleCreateView.as_view(), name="create_article"),
    path("<int:pk>/update/", AritcleUpdateView.as_view(), name="update_article"),
    path("<int:pk>/delete", ArticleDeleteView.as_view(), name="delete_article"),
]
