from django.urls import path

from . import views

urlpatterns = [
    path('<str:pizza_name>', views.get_pizza),
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
