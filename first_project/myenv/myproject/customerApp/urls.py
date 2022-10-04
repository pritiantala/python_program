"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.c_home, name='c_home'),
    path('my-cart', views.my_cart, name='my-cart'),
    path('selected-product/<int:pk>', views.selected_product, name='selected-product'),
    path('delete-product/<int:pk>', views.delete_product, name='delete-product'),
    path('plus-product/', views.plus_product, name='plus-product'),
    path('minus-product/', views.minus_product, name='minus-product'),
    path('coupon/', views.coupon, name='coupon'),
    path('proceed_checkout/', views.proceed_checkout, name='proceed_checkout'), 
]


