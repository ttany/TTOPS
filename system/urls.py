#_*_coding:utf-8_*_

from django.conf.urls import url
from system import views

from system import page_error_view
from django.conf.urls import handler404, handler500,handler403
handler404 = "system.page_error_view.page_404"
handler403 = "system.page_error_view.page_403"
handler500 = "system.page_error_view.page_500"

urlpatterns = [
    url(r'users/$', views.userIndex,name='system_users'),
    url(r'users/data/', views.userData),
    url(r'users/add/', views.userAdd),
    url(r'users/aadd/', views.addUser),
    url(r'users/edit/', views.userEdit),
    url(r'groups/$', views.groupIndex, name='system_groups'),
    url(r'groups/data/', views.groupData),
    url(r'groups/add/', views.groupAdd),


    #url(r'tables/', views.user,name='system_users'),
]