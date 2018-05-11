# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-09 06:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postid', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=32)),
                ('image', models.CharField(max_length=200)),
                ('des', models.CharField(max_length=400)),
                ('time', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=32, unique=True)),
                ('u_password', models.CharField(max_length=32)),
                ('u_email', models.CharField(max_length=64)),
                ('u_icon', models.FileField(upload_to='icons')),
            ],
        ),
        migrations.AddField(
            model_name='collect',
            name='m_postid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Movie'),
        ),
        migrations.AddField(
            model_name='collect',
            name='m_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
    ]
