from django.urls import path,include
from . import views

urlpatterns = [
    path('add/', views.add, name='添加项目'),
]