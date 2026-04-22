from django.urls import path
from . import views

urlpatterns = [
    path('', views.browse, name='home'),
    path('add/', views.add_item, name='add_item'),
    path('edit/<int:pk>/', views.edit_item, name='edit_item'),
    path('delete/<int:pk>/', views.delete_item, name='delete_item'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('closet/<str:username>/', views.public_profile, name='public_profile'),
    path('browse/', views.browse, name='browse'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('closet/', views.home, name='closet'),
]