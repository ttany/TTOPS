#_*_coding:utf-8_*_

from django.conf.urls import url
from asset import views

from system import page_error_view
from django.conf.urls import handler404, handler500,handler403
handler404 = "system.page_error_view.page_404"
handler403 = "system.page_error_view.page_403"
handler500 = "system.page_error_view.page_500"

urlpatterns = [
    url(r'asset/$', views.idcIndex,name='asset_idc'),
    #url(r'tables/', views.user,name='system_users'),
]