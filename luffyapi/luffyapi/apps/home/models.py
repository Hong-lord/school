from django.db import models

from utils.models import BaseModel


class Banner(BaseModel):
    name = models.CharField(max_length=32,verbose_name='图片名称')
    img = models.ImageField(upload_to='banner',null=True,verbose_name='轮播图位置', help_text='图片尺寸3840*800px')
    link = models.CharField(max_length=32, verbose_name='跳转链接')
    info = models.TextField(verbose_name='图片简介')

    def __str__(self):
        return self.name