"""students URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from studentsapp import views
from django.urls import include
#from test2api import views as v2
from func1api import views as v3

urlpatterns = [
    path('', include('studentsapp.urls')), #如果要到下一層去前頭的參數就要改成'students/ 取代空白
    path('admin/', admin.site.urls),
    url(r'^listone/$', views.listone),
    url(r'^listall/$', views.listall),
    url(r'^insert/$', views.insert),
    url(r'^modify/$', views.modify),
    url(r'^delete/$', views.delete),
    url(r'^index/(\w+)/$',views.index),
    url(r'^hello3/(\w+)/$',views.hello3),
    url(r'^callback/', include(('studentsapp.urls', 'studentsapp'), namespace='callback')),
  #  url(r'^callback', v2.callback),
    url(r'^callback', v3.callback),
]




