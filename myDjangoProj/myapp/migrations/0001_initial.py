# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-31 11:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_content', models.CharField(max_length=1000)),
                ('article_title', models.CharField(max_length=100)),
                ('article_description', models.CharField(blank=True, max_length=200, null=True)),
                ('article_image', models.ImageField(default='images_folder/none/no-img.jpg', upload_to='images_folder/articles')),
                ('article_date', models.DateTimeField(auto_now_add=True)),
                ('article_last_updated', models.DateTimeField(auto_now=True)),
                ('article_published', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Banned_word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=1000)),
                ('comment_published', models.BooleanField(default=False)),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_last_updated', models.DateTimeField(auto_now=True)),
                ('comment_article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Article')),
                ('comment_replay', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emotion_image', models.ImageField(default='images_folder/none/no-img.jpg', upload_to='images_folder/emotions')),
                ('emotion_expression', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='System_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=50)),
                ('user_image', models.ImageField(default='images_folder/none/no-img.jpg', upload_to='images_folder/users')),
                ('user_active', models.BooleanField(default=False)),
                ('user_marked_articles', models.ManyToManyField(blank=True, null=True, to='myapp.Article')),
            ],
        ),
        migrations.CreateModel(
            name='User_role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_type', models.CharField(max_length=30)),
                ('role_description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.User_role'),
        ),
        migrations.AddField(
            model_name='like',
            name='like_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.User'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_tags',
            field=models.ManyToManyField(blank=True, null=True, to='myapp.Tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_views',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.View'),
        ),
    ]
