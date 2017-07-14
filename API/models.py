# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db import models

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
	if created:
		Token.objects.create(user=instance)
		UserProfile.objects.create(owner=instance)

class Post(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100,blank=True,default='')
	description = models.TextField(blank=True)
	category = models.CharField(max_length=50,blank=True,default='')
	mediaFile = models.FileField(upload_to='documents/',blank=True)
	owner = models.ForeignKey('auth.User',related_name='posts',on_delete=models.CASCADE)

	class Meta:
		ordering = ('created',)


def content_file_name(instance,filename):
	return '/'.join(['profileImages',instance.owner.username,filename])


class UserProfile(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey('auth.User',related_name='profile',on_delete=models.CASCADE)
	photo= models.FileField(upload_to=content_file_name,blank=True)
	phone = models.CharField(max_length=20,blank=True,default='')
	city = models.CharField(max_length=100,blank=True,default='')
	country = models.CharField(max_length=100,blank=True,default='')
	bio = models.TextField(blank=True,default='')
	website = models.URLField(default='',blank=True)
	
	class Meta:
		ordering = ('created','owner')
