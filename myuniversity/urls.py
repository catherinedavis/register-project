from django.conf.urls import patterns, include, url
from django.contrib import admin
from register.views import *
from register import urls as reg_urls
from myuniversity.views import anonymous_required
from django.contrib.auth import views as auth_views




urlpatterns = [

    url(r'^$',Home.as_view(),name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', include(reg_urls)),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^user/login/$',anonymous_required(auth_views.login),
        {'template_name':'login.html'},name='login'),
    url(r'^user/logout/$',
        auth_views.logout,
        {'template_name': 'logout.html'},
        name='logout'),

]
