# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db import models

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
	if created:
		Token.objects.create(user=instance)

class Post(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100,blank=True,default='')
	description = models.TextField(blank=True)
	mediaFile = models.FileField(upload_to='documents/',blank=True)
	owner = models.ForeignKey('auth.User',related_name='posts',on_delete=models.CASCADE)

	class Meta:
		ordering = ('created',)