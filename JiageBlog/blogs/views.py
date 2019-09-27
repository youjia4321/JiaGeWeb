from django.shortcuts import render
from django.http import JsonResponse
from blogs.models import BlogInfo, Category, Tag
from users.models import UserProfile
from django.views.generic.base import View
from django.db.models import Q
# Create your views here.


def check(class_name, name=None):
    try:
        cate = class_name.objects.get(name=name)
        if cate:
            return cate

    except Exception as e:
        return None


class BlogListView(View):
    def get(self, request):
        blog_list = BlogInfo.objects.all().order_by('-add_time')
        all_blog = list()
        for b in blog_list:
            blog_info = dict()
            blog_info['id'] = b.id
            blog_info['title'] = b.title
            blog_info['author'] = b.author
            user_portrait = UserProfile.objects.get(Q(username=b.author) | Q(email=b.author)).portrait
            blog_info['portrait'] = str(user_portrait)
            blog_info['content'] = b.content
            blog_info['category'] = str(b.category)
            blog_info['join_time'] = str(b.add_time)
            blog_info['visit'] = b.visit
            tags = b.tag.all()
            tag_list = list()
            for t in tags:
                if t.name != "":
                    tag_list.append(t.name)
            blog_info['tags'] = tag_list
            blog_info['comment_count'] = str(len(b.blog_comments.all()))
            all_blog.append(blog_info)
        data = {'code': '200', 'data': all_blog}
        return JsonResponse({'result': data})

    def post(self, request):
        pass


def get_one_blog(request, blog_id):
    blog_detail = dict()
    blog = BlogInfo.objects.get(id=blog_id)
    blog.visit += 1
    blog.save()
    blog_detail['id'] = blog_id
    blog_detail['title'] = blog.title
    blog_detail['author'] = blog.author
    user_portrait = UserProfile.objects.get(Q(username=blog.author) | Q(email=blog.author)).portrait
    blog_detail['portrait'] = str(user_portrait)
    blog_detail['content'] = blog.content
    blog_detail['category'] = str(blog.category)
    blog_detail['join_time'] = str(blog.add_time)
    blog_detail['visit'] = blog.visit
    tags = blog.tag.all()
    tag_list = list()
    for t in tags:
        if t.name != "":
            tag_list.append(t.name)
    blog_detail['tags'] = tag_list
    blog_detail['comment_count'] = str(len(blog.blog_comments.all()))
    data = {'code': '200', 'data': blog_detail}
    return JsonResponse({'result': data})


def add_blog(request):
    try:
        title = request.POST.get('title', '')
        author = request.POST.get('author', '')
        content = request.POST.get('content', '')
        category = request.POST.get('category', '')
        tag = request.POST.get('tag', '')
        tag_list = tag.split(' ')
        cate = check(Category, name=category)
        # 处理分类
        if cate is not None:
            # 存在此分类，就在blog创建时加上此分类
            blog = BlogInfo.objects.create(title=title, author=author, content=content, category=cate)
        else:
            # 反之，先创建分类，再添加到blog
            cate = Category.objects.create(name=category)
            blog = BlogInfo.objects.create(title=title, author=author, content=content, category=cate)
        # 处理标签
        for _t in tag_list:
            _tag = check(Tag, name=_t)
            # 检查是否存在这个标签对象
            if _tag is not None:
                # 如果存在 not None，就添加这个对象到当前blog
                blog.tag.add(_tag)
            else:
                # 不存在，先在Tag模型创建一个对象，再添加到当前blog
                t = Tag.objects.create(name=_t)
                blog.tag.add(t)
        data = {'code': '200', 'msg': '发布成功'}
        return JsonResponse({'result': data})
    except Exception as e:
        data = {'code': '10001', 'msg': '发布失败'}
        return JsonResponse({'result': data})
