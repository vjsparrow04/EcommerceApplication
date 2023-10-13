"""ecomm URL Configuration

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
from extra import  views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('extra',include('extra.urls')),

    path('',views.index,name='home'),

    path('register/',views.register,name='register'),
    path('log/',views.log,name='log'),
    path('logout',views.logout,name='logout'),
    path('contact',views.contact,name='contact'),                    
   
    path('productview',views.productview,name='productview'), 
    path('payment',views.payment,name='payment'),
    path('productin',views.productin,name='productin'),
    path('blog',views.blog,name='blog'),

     path('productin/<str:slug>/', views.productin, name='productin'),
     



]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
