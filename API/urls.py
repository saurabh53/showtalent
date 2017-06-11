from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static

from . import views as local_views
from rest_framework.authtoken import views as rest_framework_views

urlpatterns=[

	url(r'^login/$',local_views.get_auth_token,name='login'),
	url(r'^logout/$',local_views.logout_user,name='logout'),
	url(r'^auth/',include('rest_framework.urls',namespace='rest_framework')),
	url(r'^get_auth_token/$',rest_framework_views.obtain_auth_token,name='get_auth_token'),
	url(r'^users/$', local_views.UserRegistration.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', local_views.UserList.as_view()),
	url(r'^posts/$', local_views.PostList.as_view()),
	url(r'^posts/category/$', local_views.PostListOnCategory.as_view()),
	url(r'^posts/query/$', local_views.get_query,name='get_query'),
	url(r'^posts/(?P<pk>[0-9]+)/$', local_views.PostDetail.as_view()),
	url(r'^profile/(?P<pk>[0-9]+)/$', local_views.ProfileDetail.as_view()),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
