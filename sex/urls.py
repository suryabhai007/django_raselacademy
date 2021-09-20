from django.urls import path

from . import views

app_name = 'sex'

urlpatterns = [
    path('category/<str:name>/', views.category, name="category"),
    path('blogger/<str:title>/', views.blogger, name="blogger"),
    path('blog/comment/<str:title>', views.comment, name="comment"),
    path('', views.index, name="index")
    ]
