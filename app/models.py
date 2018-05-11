from django.db import models

# Create your models here.
class User(models.Model):
    u_name = models.CharField(max_length=32, unique=True)
    u_password = models.CharField(max_length=32)
    u_email = models.CharField(max_length=64)
    u_icon = models.FileField(upload_to='icons')


class Movie(models.Model):
    postid = models.IntegerField(unique=True)
    title = models.CharField(max_length=32)
    image = models.CharField(max_length=200)
    des = models.CharField(max_length=400)
    time = models.CharField(max_length=16)


class Collect(models.Model):
    m_user = models.ForeignKey(User)
    m_postid = models.ForeignKey(Movie)

class Banner(models.Model):
    img_url = models.CharField(max_length=200)