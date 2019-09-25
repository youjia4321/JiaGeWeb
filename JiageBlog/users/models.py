from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# from blogs.models import BlogInfo
# Create your models here.


class UserProfile(AbstractUser):
    portrait = models.ImageField(upload_to="person", default='person/default.jpg', max_length=100, verbose_name='用户头像')
    gender = models.CharField(max_length=6, choices=(('男', '男'), ('女', '女')), default='female', verbose_name='性别')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    # favorite = models.ManyToManyField(BlogInfo, verbose_name='收藏博客', default='')

    class Meta:
        db_table = 'user_profile'
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
