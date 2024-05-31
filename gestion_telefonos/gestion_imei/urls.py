# gestion_imei/urls.py
from django.urls import path
from .views import cell_list, cell_create, cell_edit,login_view,logout_view,register_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('', cell_list, name='cell_list'),
    path('create/', cell_create, name='cell_create'),
    path('edit/<int:pk>/', cell_edit, name='cell_edit'),
]
