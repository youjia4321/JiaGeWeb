"""JiageBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from users import views as user
from blogs import views as blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user.index, name='index'),
    path('api/userLogin', user.user_login, name='userLogin'),
    path('api/userRegister', user.register_account, name='userRegister'),
    path('api/addBlog', blog.add_blog, name='addBlog'),
    path('api/listOfBlog', blog.BlogListView.as_view(), name='listOfBlog'),
    path('api/commentOfBlog', blog.comment_blog, name='commentOfBlog'),
    path('api/selfOfBlog', blog.self_blog, name='selfOfBlog'),
    path('api/delOfBlog', blog.delete, name='delOfBlog'),
    path('api/centerManage', blog.center_manage, name='centerManage'),
    path('api/uploadAvatar', blog.upload_avatar, name='uploadAvatar'),
    path('api/blogSave', blog.edit_post_save, name='blogSave'),
    path('api/allCategory', blog.get_all_category, name='allCategory'),
    path('api/getChooseCategory', blog.get_choose_cate, name='getChooseCategory'),
    url(r'^api/blog/(\d+)/$', blog.get_one_blog, name='oneBlog'),
    url(r'^api/edit/(\d+)/$', blog.edit_blog, name='editBlog'),
    url(r'^static/(?P<path>.*)/$', serve, {"document_root": settings.STATIC_ROOT}, name='static'),
    url(r'^media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}, name='media'),
]
