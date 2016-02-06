from django.conf.urls import patterns, include, url
from register import views
from register.views import *
from register.models import *

urlpatterns = [

    url(r'^signup/$', UserRegistrationView.as_view(), name='signup'),
    url(r'^user/success/$', UserRegistrationSuccessView.as_view(), name='signup_success'),
    url(r'^signIn/$', UserRegistrationView.as_view(), name='login'),
    url(r'^logout/$', UserRegistrationView.as_view(), name='logout'),
    url(r'^dash/$', UserDashboardView.as_view(), name='dash'),
        ]