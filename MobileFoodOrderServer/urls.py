from django.conf.urls import patterns, include, url
from django.contrib import admin

from order import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MobileFoodOrderServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # ex: /admin
    # url(r'^admin/', include(admin.site.urls)),

    # ex: /
    url(r'^$', views.IndexView.as_view(), name="home"),

    # ex: /user
    # url(r'^user/$', views.UserView.as_view(), name='user'),

    # ex: /regist
    url(r'^regist/$', views.RegistView.as_view(), name='regist'),

    # ex: /order
    url(r'^order/$', views.OrderView.as_view(), name='order'),

    # ex: /info
    url(r'^info/$', views.InfoView.as_view(), name='info'),

    # ex: /login
    url(r'^login/$', views.login, name='login'),

    # ex: /logout
    url(r'^logout/$', views.logout, name='logout'),

    # ex: /regist
    url(r'^register/$', views.register, name='register'),
)
