from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login', views.login, name="login"),
    url(r'^sign_up', views.sign_up, name="sign_up"),
    # url(r'^dps', views.dps_redirect, name="dps")
]
