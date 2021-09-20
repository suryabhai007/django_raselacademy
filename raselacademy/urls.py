from django.views import generic
from django.urls import path
from . import views
from . feeds import LatestBlogsFeed
app_name = 'raselacademy'
urlpatterns = [
    path("", views.index, name="index"),
    path("blog_api", views.blog_api, name="blog_api"),
    path("feed/rss/", LatestBlogsFeed(), name="LatestBlogsFeed"),
    path("success/", views.success, name="success"),
    path("categories/<str:name>", views.categories, name="categories"),
    
    path("Blog/<str:title>", views.blog, name="blog"),

    
    ]
