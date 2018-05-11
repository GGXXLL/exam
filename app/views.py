import hashlib

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from django.urls import reverse
from app.models import *


def home(request):
    banners = Banner.objects.all()
    movies = Movie.objects.all()
    data = {
        'banners': banners,
        'movies': movies,
    }
    return render(request, 'home.html', context=data)


def logined(request):
    banners = Banner.objects.all()
    movies = Movie.objects.all()

    data = {
        'banners': banners,
        'movies': movies,
        'movies_collect':[],
    }
    username = request.session.get('username')
    if username:
        user = User.objects.get(u_name=username)
        movies_collect =Collect.objects.filter(m_user=user)
        if movies_collect.exists():
            for movie in movies_collect:
                data['movies_collect'].append(movie.m_postid)
        data['user'] = user
    return render(request, 'home_logined.html', context=data)


def collect(request):
    banners = Banner.objects.all()
    username = request.session.get('username')
    user = User.objects.filter(u_name=username).first()
    data = {
        'banners': banners,
        'user': user,
        'movies': [],
    }
    movies = Collect.objects.filter(m_user=user)
    if movies.exists():
        for movie in movies:
            data['movies'].append(movie.m_postid)
    return render(request, 'home_logined_collected.html', context=data)


def userinfo(request):
    username = request.session.get('username')
    user = User.objects.get(u_name=username)
    if request.method == 'POST':
        user.u_icon = request.FILES['icon']
        user.save()
    elif request.method == 'GET':
        data = {
            'user': user
        }
        return render(request, 'userinfo_mod.html', context=data)
    return redirect(reverse('app:logined'))


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        # print(username)
        error = ''
        password = request.POST.get("password")
        users = User.objects.filter(Q(u_name=username) | Q(u_email=username))
        if users.exists():
            user = users.first()
            u_password = user.u_password
            if u_password == password:
                request.session["username"] = user.u_name
                return redirect(reverse("app:logined"))
        error = 'error'
        return render(request, 'login.html', {'error': error})

    elif request.method == "GET":
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES['icon']
        # 密码安全
        password = passwordmd5(password)

        user = User()
        user.u_name = username
        user.u_password = password
        user.u_email = email
        user.u_icon = icon
        user.save()
        resp = redirect(reverse('app:logined'))
        request.session['username'] = username
        return resp
    elif request.method == 'GET':
        return render(request, 'register.html')


def passwordmd5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


def checkUser(request):
    username = request.GET.get('username')
    user = User.objects.filter(u_name=username)
    data = {
        'msg': '用户名可用',
    }
    if user.exists():
        data['msg'] = '用户名已存在'
    return JsonResponse(data)


def addmovie(request):
    username = request.session.get('username')
    user = User.objects.get(u_name=username)
    data = {
        'status': '200',
    }
    postid = request.GET.get('postid')
    p_id = Movie.objects.filter(postid=postid).first()
    movie = Collect.objects.filter(Q(m_postid=p_id) & Q(m_user=user))
    if not movie.exists():
        m = Collect()
        m.m_postid = p_id
        m.m_user = user
        m.save()
    else:
        movie.delete()
        data['status'] = '300'
    return JsonResponse(data)


def logout(request):
    resp = redirect(reverse('app:home'))
    request.session.delete()
    return resp