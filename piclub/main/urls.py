from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^main', views.index, name="index"),
    url(r'^login', views.login, name="login"),
    url(r'^sign_up', views.sign_up, name="sign_up"),
    url(r'^about', views.about, name="about")
]
