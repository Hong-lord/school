"""luffyapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path,include
from django.views.static import serve
from django.conf import settings
# from luffyapi.apps.home import views
from . import views

from rest_framework.routers import SimpleRouter
import xadmin
router = SimpleRouter()
router.register('banner',views.BannerView,'banner')

urlpatterns = [

    # path('Banner/', views.BannerView.as_view()),
    path('', include(router.urls)),

]
