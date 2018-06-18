"""zad3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from spoldzielnia import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^show/(?P<flatid>\w+)/$', views.indexshow, name='indexshow'),
    url(r'^edit/(?P<flatid>\w+)/$', views.indexedit, name='indexedit'),
    url(r'^update/(?P<flatid>\w+)/$', views.indexupdate, name='indexupdate'),
    url(r'^new/$', views.indexnew, name='indexnew'),
    url(r'^create/$', views.indexcreate, name='indexcreate'),
    url(r'^destroy/(?P<flatid>\w+)/$', views.indexdestroy, name='indexdestroy'),

    url(r'^resident/$', views.resident, name='resident'),
    url(r'^resident/show/(?P<residentid>\w+)/$', views.residentshow, name='residentshow'),
    url(r'^resident/new/(?P<flatid>\w+)/$', views.residentnew, name='residentnew'),
    url(r'^resident/create/(?P<flatid>\w+)/$', views.residentcreate, name='residentcreate'),
    url(r'^resident/edit/(?P<residentid>\w+)/$', views.residentedit, name='residentedit'),
    url(r'^resident/update/(?P<residentid>\w+)/$', views.residentupdate, name='residentupdate'),
    url(r'^resident/destroy/(?P<residentid>\w+)/$', views.residentdestroy, name='residentdestroy'),

    url(r'^payment/show/(?P<paymentid>\w+)/$', views.paymentshow, name='paymentshow'),
    url(r'^payment/new/(?P<residentid>\w+)/$', views.paymentnew, name='paymentnew'),
    url(r'^payment/create/(?P<residentid>\w+)/$', views.paymentcreate, name='paymentcreate'),
    url(r'^payment/edit/(?P<paymentid>\w+)/$', views.paymentedit, name='paymentedit'),
    url(r'^payment/update/(?P<paymentid>\w+)/$', views.paymentupdate, name='paymentupdate'),
    url(r'^payment/destroy/(?P<paymentid>\w+)/$', views.paymentdestroy, name='paymentdestroy'),

    path('admin/', admin.site.urls),
]
