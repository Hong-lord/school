from django.shortcuts import render,HttpResponse

# Create your views here.
from rest_framework.views import APIView
from luffyapi.utils.response import APIResponse
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet

from . import models
from . import serializer

"""
通过继承GenericAPIView，对类的queryset与serializer_class属性赋值，
然后get方法可以调用父类的ListModelMixin方法的list()方法，
而post方法可以调用父类CreateModelMixin的方法，其他URL分发等与之前的APIView类似
"""
# 方法一:路由配置 path('Banner/', views.BannerView.as_view()),
# class BannerView(GenericAPIView,ListModelMixin):
#     queryset = models.Banner.objects.filter(is_delete=False,is_show=True).order_by('display_order')
#     serializer_class = serializer.BannerModelSerializer


"""
# from rest_framework.routers import SimpleRouter
#
# router = SimpleRouter()
# router.register('banner',views.BannerView,'banner')
#
# urlpatterns = [
#     # path('Banner/', views.BannerView.as_view()),
#     path('', include(router.urls)),
#
# ]
"""
from django.conf import settings
# 上面是他的路由配置
class BannerView(GenericViewSet,ListModelMixin):
    # 无论后边有多少待展示的,最多就展示三条
    queryset = models.Banner.objects.filter(is_delete=False,is_show=True).order_by('display_order')[:settings.BANNER_COUNTER]
    serializer_class = serializer.BannerModelSerializer