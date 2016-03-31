from __future__ import unicode_literals
from django.contrib.auth.models import *
from django.db import models

# Create your models here.
class Tag(models.Model):
	tag_name=models.CharField(max_length=20)
	def __str__(self):
		return self.tag_name

class View(models.Model):
	view_user_id=models.ForeignKey(User,on_delete=models.CASCADE)

class Article(models.Model):
	article_content=models.CharField(max_length=1000)
	article_title=models.CharField(max_length=100)
	article_description=models.CharField(max_length=200,null=True,blank=True)
	article_image=models.ImageField(upload_to = 'images_folder/articles' , default = 'images_folder/none/no-img.jpg')
	article_date=models.DateTimeField(auto_now_add=True , auto_now=False)
	article_last_updated=models.DateTimeField(auto_now_add=False ,auto_now=True)
	article_published=models.BooleanField(default=False)
	article_views=models.ForeignKey(View,on_delete=models.CASCADE,null=True,blank=True)
	article_tags = models.ManyToManyField(Tag,null=True,blank=True)
	def __str__(self):
		return self.article_content



class User_role(models.Model):
	role_type=models.CharField(max_length=30)
	role_description=models.CharField(max_length=100,null=True,blank=True)
	def __str__(self):
		return self.role_type

class User(models.Model):
	user_name=models.CharField(max_length=100)
	user_email=models.EmailField()
	user_password=models.CharField(max_length=50)
	user_image=models.ImageField(upload_to = 'images_folder/users' , default = 'images_folder/none/no-img.jpg')
	user_active=models.BooleanField(default=False)
	user_role=models.ForeignKey(User_role,on_delete=models.CASCADE)
	user_marked_articles = models.ManyToManyField(Article,null=True,blank=True)
	def __str__(self):
		return self.name

class Comment(models.Model):
	comment_content=models.CharField(max_length=1000)
	comment_user_id=models.ForeignKey(User,on_delete=models.CASCADE)
	comment_article_id=models.ForeignKey(Article,on_delete=models.CASCADE)
	comment_published=models.BooleanField(default=False)
	comment_date=models.DateTimeField(auto_now_add=True)
	comment_last_updated=models.DateTimeField(auto_now_add=False,auto_now=True)
	comment_replay = models.OneToOneField('self',null=True,blank=True)
	def __str__(self):
		return self.comment_content		

class Like(models.Model):
	like_user_id=models.ForeignKey(User,on_delete=models.CASCADE)
	like_comment_id=models.ForeignKey(Comment,on_delete=models.CASCADE)

class Banned_word(models.Model):
	word=models.CharField(max_length=20)
	def __str__(self):
		return self.word

class Emotion(models.Model):
	emotion_image=models.ImageField(upload_to = 'images_folder/emotions' , default = 'images_folder/none/no-img.jpg')
	emotion_expression=models.CharField(max_length=10)
	def __str__(self):
		return self.emotion_image

class System_status(models.Model):
	status=models.BooleanField(default=False)
	def __str__(self):
		return self.status
