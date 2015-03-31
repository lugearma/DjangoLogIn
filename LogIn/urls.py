from django.conf.urls import patterns, include, url
from django.contrib import admin
from SimpleApp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LogIn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^auth/(?P<provider_name>\w*)', views.login, name='login'),
    # url(r'^auth/twitter', views.login),
    url(r'^auth/twitter/callback', views.simpleApp),

)
