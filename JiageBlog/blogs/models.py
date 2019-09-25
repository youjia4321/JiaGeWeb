from django.db import models
from datetime import datetime
from users.models import UserProfile
# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name='名称', max_length=100)

    class Meta:
        db_table = 'blog_category'
        verbose_name = "类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name='名称', max_length=100)

    class Meta:
        db_table = 'blog_tag'
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BlogInfo(models.Model):
    title = models.CharField(verbose_name='博客标题', max_length=150)
    author = models.CharField(verbose_name='作者', max_length=20, default='')
    content = models.TextField(verbose_name='博客正文')
    visit = models.IntegerField(default=0, verbose_name='浏览量')
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE, null=True, blank=True)
    # 多对一（博客--类别）
    tag = models.ManyToManyField(Tag, verbose_name='标签', default='')  # (多对多）
    add_time = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)

    class Meta:
        db_table = 'blog_info'
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(BlogInfo, verbose_name='博客', on_delete=models.CASCADE)  # (博客--评论:一对多)
    name = models.CharField(verbose_name='称呼', max_length=50)
    email = models.EmailField(verbose_name='邮箱')
    content = models.CharField(verbose_name='内容', max_length=500)
    pub = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)

    class Meta:
        db_table = 'blog_comment'
        verbose_name = "评论"
        verbose_name_plural = "评论"

    def __str__(self):
        return str(self.blog)
