from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('signin/', views.signin, name='signin'),
    path('sat_det/', views.sat_det, name='sat_det'),
    path('detail/', views.detail, name='detail'),
    path('satellite/link/<str:name>/', views.link, name='link'),
    path('manage/', views.manage, name='manage'),
    path('category/<str:i>/', views.category, name='category'),
    path('logout/', views.logout, name='logout')

]

