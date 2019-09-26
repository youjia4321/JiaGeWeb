from django.contrib import admin
from blogs.models import BlogInfo, Category, Tag, Comment
# Register your models here.


class BlogInfoAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "add_time")


admin.site.register(BlogInfo, BlogInfoAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
