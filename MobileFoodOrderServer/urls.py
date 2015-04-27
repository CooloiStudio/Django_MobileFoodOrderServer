from django.conf.urls import patterns, include, url
from django.contrib import admin

from order import views, client, canteen, food, order

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MobileFoodOrderServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # ex: /admin
    # url(r'^admin/', include(admin.site.urls)),

    # ex: /
    url(r'^$', views.IndexView.as_view(), name="home"),

    # ex: /regist
    url(r'^regist/$', views.RegistView.as_view(), name='regist'),

    # ex: /accounts/login
    (r'^accounts/login/$', views.InfoView.as_view()),

    # ex: /info
    url(r'^info/$', views.InfoView.as_view(), name='info'),

    # ex: /login
    url(r'^login/$', views.login, name='login'),

    # ex: /changepw
    url(r'^changepw', views.changepw, name='changepw'),

    # ex: /logout
    url(r'^logout/$', views.logout, name='logout'),

    # ex: /regist
    url(r'^register/$', views.register, name='register'),

    # client
    # ex: /clientregist
    url(r'^clientregist/$', client.register, name='clientregist'),

    # ex: /clientlogin
    url(r'^clientlogin/$', client.login, name='clientlogin'),

    # ex: /clientlogout
    url(r'^clientlogout/$', client.logout, name='clientlogout'),

    # ex: /clientuserinfo
    url(r'^clientuserinfo/$', client.userinfo, name='clientuserinfo'),

    # ex: /clientfood
    url(r'^clientfood/$', client.food, name='food'),

    # canteen
    # ex: /canteen
    url(r'^canteen/$', canteen.CanteenView.as_view(), name='canteen'),

    # ex: /canteencreate
    url(r'^canteencreate/$', canteen.create, name='canteencreate'),

    # food
    # ex: /food
    url(r'^food/$', food.FoodView.as_view(), name='food'),

    # ex: /foodcreate
    url(r'^foodcreate/$', food.create, name='foodcreate'),

    # order
    # ex: /order
    url(r'^order/$', order.OrderView.as_view(), name='order'),

    # ex: /orderconfirm
    url(r'^orderconfirm/$', order.confirm, name='orderconfirm'),

    # ex: /orderdeal
    url(r'^orderdeal/$', order.deal, name='orderdeal'),
)
