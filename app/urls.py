from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^home/', views.home, name='home'),
    url(r'^logined/', views.logined, name='logined'),
    url(r'^collect/', views.collect, name='collect'),
    url(r'^userinfo/', views.userinfo, name='userinfo'),
    url(r'^checkuser/', views.checkUser, name='checkUser'),
    url(r'^addmovie/', views.addmovie, name='addmovie'),
    url(r'^logout/', views.logout, name='logout'),
]
