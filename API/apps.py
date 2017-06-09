# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.conf import settings
from API.trie import *




class ApiConfig(AppConfig):
    name = 'API'
    def ready(self):
		from API.models import Post
		settings.TRIE = Trie()
		test = Post.objects.all()
		array = [None]
		for t in test:
			array.append(t.category)
		words = 'hello goodbye help gerald gold tea ted team to too tom stan standard money'
		for word in array:
			if word!=None:
				settings.TRIE.add(word)
		# settings.TRIE.add('goodbye in trie: ')
		# print 'goodbye in trie: ',settings.TRIE.has_word('goodbye in trie: ')
		# print settings.TRIE.start_with_prefix('goodbye')
		# print settings.TRIE.start_with_prefix('t')	

