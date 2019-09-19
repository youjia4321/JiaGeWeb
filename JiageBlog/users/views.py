from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from users.models import UserProfile
from django.contrib.auth.hashers import make_password
from django.db.models import Q
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
            avatar = user.portrait
            print(avatar)
            data = {'code': '200', 'msg': '登录成功', 'avatar': str(avatar)}
            return JsonResponse({'result': data})
        else:
            data = {'code': '10001', 'msg': '密码错误'}
            return JsonResponse({'result': data})
    else:
        data = {'code': '404', 'msg': '用户不存在'}
        return JsonResponse({'result': data})
