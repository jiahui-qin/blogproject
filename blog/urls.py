from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views



app_name = 'blog'
urlpatterns = [
    url(r'^recalter/$', views.recalter, name='recalter'),
    url(r'^bactalter/$', views.bactalter, name='bactalter'),
    url(r'^cpdalter/$', views.cpdalter, name='cpdalter'),
    url(r'^crualter/$', views.crualter, name='crualter'),

    url(r'^index/$', views.recordindex, name='index'),
    url(r'^bactindex/$', views.bactindex, name='bactindex'),
    url(r'^recordindex/$', views.recordindex, name = 'recordindex'),
    url(r'^crudeexindex/$', views.crudeexindex, name='crudeexindex'),
    url(r'^cpdindex/$', views.cpdindex, name='cpdindex'),

    url(r'^upload/$', views.upload, name='upload'),
    url(r'^bactload/$', views.bactload, name='bactload'),
    url(r'^cpdload/$', views.cpdload, name='cpdload'),
    url(r'^curdeexupload/$', views.curdeexupload, name='curdeexupload'),

    url(r'^recdel/$', views.recdel, name='recdel'),
    url(r'^bactdel/$', views.bactdel, name='bactdel'),
    url(r'^cpddel/$', views.cpddel, name='cpddel'),
    url(r'^crudel/$', views.crudel, name='crudel'),


    url(r'^accounts/login/$', views.login_user, name = 'login_user'),
    url(r'^accounts/logout/$', views.logout_user, name = 'logout_user'),

    url(r'^bact/bact2cru/(\d+)$', views.bact2cru, name='bact2cru'),

    #url(r'^managedata/$', views.managedata, name = 'managedata'),
]