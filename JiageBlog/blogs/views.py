from django.http import JsonResponse
from blogs.models import BlogInfo, Category, Tag, Comment
from users.models import UserProfile
from django.views.generic.base import View
from django.db.models import Q
from django.conf import settings
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
    comments = blog.blog_comments.all().order_by('-pub')
    comments_list = list()
    for c in comments:
        comment = dict()
        comment['author'] = c.name
        comment_portrait = UserProfile.objects.get(Q(username=c.name) | Q(email=c.name)).portrait
        comment['portrait'] = str(comment_portrait)
        comment['content'] = c.content
        comment['pub'] = str(c.pub)
        comments_list.append(comment)
    data = {'code': '200', 'data': blog_detail, 'comments': comments_list}
    return JsonResponse({'result': data})


def comment_blog(request):
    blog_id = request.POST.get('id', '')
    blog = BlogInfo.objects.get(id=blog_id)
    username = request.POST.get('name', '')
    content = request.POST.get('content', '')
    user = UserProfile.objects.get(Q(username=username) | Q(email=username))
    name = user.username
    email = user.email
    Comment.objects.create(blog=blog, name=name, email=email, content=content)
    data = {'code': '200'}
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


def self_blog(request):
    author = request.POST.get('author', '')
    user = UserProfile.objects.get(Q(username=author) | Q(email=author))
    blog_list = BlogInfo.objects.filter(Q(author=user.username) | Q(author=user.email)).order_by('-add_time')
    all_blog = list()
    for b in blog_list:
        blog = dict()
        blog['id'] = b.id
        blog['title'] = b.title
        blog['author'] = b.author
        blog['portrait'] = str(user.portrait)
        blog['content'] = b.content
        blog['category'] = str(b.category)
        blog['join_time'] = str(b.add_time)
        blog['visit'] = b.visit
        tags = b.tag.all()
        tag_list = list()
        for t in tags:
            if t.name != "":
                tag_list.append(t.name)
        blog['tags'] = tag_list
        blog['comment_count'] = str(len(b.blog_comments.all()))
        all_blog.append(blog)
    data = {'code': '200', 'data': all_blog}
    return JsonResponse({'result': data})


def delete(request):
    blog_id = request.POST.get('blog_id', '')
    blog = BlogInfo.objects.get(id=blog_id)
    blog.delete()
    data = {'code': '200', 'msg': '删除成功'}
    return JsonResponse({'result': data})


def center_manage(request):
    author = request.POST.get('author', '')
    user = UserProfile.objects.get(Q(username=author) | Q(email=author))
    person = dict()
    person['username'] = user.username
    person['gender'] = user.gender
    person['mobile'] = user.mobile
    person['email'] = user.email
    person['portrait'] = str(user.portrait)
    data = {'code': '200', 'data': person}
    return JsonResponse({'result': data})


def upload_avatar(request):
    file = request.FILES.get('file', '')
    author = request.POST.get('author', '')
    img_addr = '%s/person/%s' % (settings.MEDIA_ROOT, file.name)
    # 写入文件
    with open(img_addr, 'wb') as f:
        for f_img in file.chunks():
            f.write(f_img)
    user = UserProfile.objects.get(Q(username=author) | Q(email=author))
    user.portrait = 'person/'+file.name
    user.save()
    data = {'code': '200', 'msg': '修改头像成功'}
    return JsonResponse({'result': data})


def edit_blog(request, blog_id):
    blog = BlogInfo.objects.get(id=blog_id)
    title = blog.title
    content = blog.content
    data = {'code': '200', 'title': title, 'content': content}
    return JsonResponse({'result': data})


def edit_post_save(request):
    blog_id = request.POST.get('id', '')
    title = request.POST.get('title', '')
    content = request.POST.get('content', '')
    content = request.POST.get('content', '')
    blog_info = BlogInfo.objects.get(id=blog_id)
    blog_info.title = title
    blog_info.content = content
    blog_info.save()
    return JsonResponse({'result': {'code': '200', 'msg': '编辑成功'}})


def get_all_category(request):
    cate_list = Category.objects.all()
    all_cate = []
    for c in cate_list:
        all_cate.append(c.name)
    return JsonResponse({'result': {'code': '200', 'all_cate': all_cate}})


def get_choose_cate(request):
    cate = request.POST.get('cate', '')
    category = Category.objects.get(name=cate)
    blog_list = category.category_blogs.all()
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
