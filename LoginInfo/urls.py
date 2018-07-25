
from django.conf.urls import include, url
from django.contrib import admin
from LoginInfo import views


urlpatterns = [
    url(r'^login$', views.login),
    url(r'^logincheck$',views.logincheck),
    url(r'^index$',views.index),

    url(r'^register$',views.register),
    url(r'^registercheck$',views.registercheck),
]
