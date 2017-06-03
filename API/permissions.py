from rest_framework import permissions
from rest_framework.authtoken.models import Token

class IsOwnerOrReadOnly(permissions.BasePermission):

	def has_object_permission(self,request,view,obj):
		tokens = Token.objects.all()
		if request.META.get('HTTP_AUTHENTICATION')==None:
			print 'return'
			return False
		else:
			data = request.META.get('HTTP_AUTHENTICATION').strip().split(' ')
			if len(data)!=2:
				print 'length'
				return False
			if data[0]!='Token':
				print 'Token',data[0],data[1]
				return False
			if data[1] not in tokens:
				print 'Not Available',data[1]
				print tokens
				return False
		return True
