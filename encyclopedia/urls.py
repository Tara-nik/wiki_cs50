from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('wiki/<str:title>/', views.entry_detail, name='entry_detail'),
    path('create/', views.create_new_entry, name='create_new_entry'),
    path('edit/<str:title>/', views.edit_entry, name='edit'),
    path('random/', views.random_page, name='random_page'),
]