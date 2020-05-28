from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("blogs/", views.BlogListView.as_view(), name="blogs"),
    path("bloggers/", views.AuthorListView.as_view(), name="bloggers"),
    re_path(
        r"^blogs/(?P<pk>\d+)$",
        views.BlogDetailView.as_view(),
        name="blog-detail",
    ),
    re_path(
        r"^bloggers/(?P<pk>\d+)$",
        views.AuthorDetailView.as_view(),
        name="author-detail",
    ),
]
