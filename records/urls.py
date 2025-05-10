from django.urls import path
from . import views

urlpatterns = [
    path('', views.record_list, name='record_list'),
    path('add/', views.record_add, name='record_add'),
    path('edit/<int:pk>/', views.record_edit, name='record_edit'),
    path('delete/<int:pk>/', views.record_delete, name='record_delete'),
] 