from django.conf.urls import patterns, include, url
from django.contrib import admin
from SimpleApp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LogIn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hola/', views.holaMundo),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^/', views.home, name='home'),
    #url(r'^login/(\w*)', views.login, name='login'),
    #url(r'^simpleApp/' include(SimpleApp)),

)
