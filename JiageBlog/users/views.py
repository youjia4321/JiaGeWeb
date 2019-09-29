from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from users.models import UserProfile
from django.contrib.auth.hashers import make_password
from django.db.models import Q
import re
# Create your views here.


def index(request):
    return HttpResponse("Hello, CSND")


def check(username=None, password=None):
    try:
        user = UserProfile.objects.get(Q(username__exact=username) | Q(email__exact=username))
        # 用户可以用email和username进行登录，引用Q 相当于or
        if user.check_password(password):
            return user
        else:
            return False
    except Exception as e:
        return None


def user_login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = check(username=username, password=password)
    if user is not None:
        if user is not False:
            username = user.username
            avatar = user.portrait
            data = {'code': '200', 'msg': '登录成功', 'username': username, 'avatar': str(avatar)}
            return JsonResponse({'result': data})
        else:
            data = {'code': '10001', 'msg': '密码错误'}
            return JsonResponse({'result': data})
    else:
        data = {'code': '404', 'msg': '用户不存在'}
        return JsonResponse({'result': data})


# 判断邮箱格式
def is_valid_email(addr):
    valid_str = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
    if re.match(valid_str, addr):
        return True
    else:
        return False


def register_account(request):
    email = request.POST.get('email', '')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    valid_email = is_valid_email(email)
    if not valid_email:
        data = {'code': '10001', 'msg': '邮箱格式不正确'}
        return JsonResponse({'result': data})
    if UserProfile.objects.filter(email=email):
        data = {'code': '10001', 'msg': '用户已存在'}
        return JsonResponse({'result': data})
    if UserProfile.objects.filter(username=username):
        data = {'code': '10001', 'msg': '用户名已被使用'}
        return JsonResponse({'result': data})
    secret_password = make_password(password)
    UserProfile.objects.create(username=username, email=email, password=secret_password)
    data = {'code': '200', 'msg': '注册账号成功'}
    return JsonResponse({'result': data})