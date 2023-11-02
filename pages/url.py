from django.urls import path
from .views import (
    homePageView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    path("", homePageView.as_view(), name="home"),
    path("<int:pk>", BlogDetailView.as_view(), name="post_detail"),
    path("post/new", BlogCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/edit", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete", BlogDeleteView.as_view(), name="post_delete"),
]
