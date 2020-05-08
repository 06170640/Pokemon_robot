from django.urls import path
from django.conf.urls import url
from django.conf.urls import include

from . import views
#from django.urls import include
app_name='studentsapp'
urlpatterns = [
    path('', views.index, name='index'),
   # path('callback/', include('studentsapp.urls')),
     url('callback/', include('studentsapp.urls')),
     path('',views.callback,name='callback'),
     #path('',views.handl_message,name='handl_message'),
]
