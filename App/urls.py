from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug>/', views.ctg, name='category_one'),
    path('view/<int:pk>/', views.view, name='views_one'),
    path('search/', views.search, name='search'),
    path('contact/',views.contact,name='contact')
]

