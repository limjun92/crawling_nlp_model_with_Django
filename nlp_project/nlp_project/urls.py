"""nlp_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from app_crawling import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('crawling/', views.crawling, name='crawling'),
    path('get_title/', views.get_title, name='get_title'),
    path('comment/<str:video_id>/<str:keyword>', views.comment,name = 'comment'),
    path('save/<str:keyword>',views.save,name='save'),
    path('model',views.model, name = 'model'),
    path('get_csv/<str:csv>',views.get_csv, name = 'get_csv'),
    path('create_model',views.create_model,name = 'create_model'),
    path('use_model/<str:name>',views.use_model,name = 'use_model'),
    path('connect_model/<str:name>',views.connect_model,name = 'connect_model'),
]
