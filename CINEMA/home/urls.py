from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('titles/<id>/',views.titles,name='titles'),
    path('lists/<typ>',views.lists,name='lists'),
    path('add/<arg>',views.add_list,name='add_list'),
    path('remove/<arg>',views.rm_list,name='rm_list'),
]
