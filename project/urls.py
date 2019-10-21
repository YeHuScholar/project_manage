from django.urls import path
from . import views

urlpatterns = [
    path('project_list/', views.project_list, name='项目列表'),
    path('add/', views.add, name='添加项目'),
    path('<int:project_id>', views.detail, name="项目细节")
]