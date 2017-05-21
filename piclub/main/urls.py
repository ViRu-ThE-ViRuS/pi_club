from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^home', views.index, name="index"),
    url(r'^main', views.index, name="index"),
    url(r'^login', views.login, name="login"),
    url(r'^sign_up', views.sign_up, name="sign_up"),
    url(r'^about', views.about, name="about"),
    url(r'^contact_us', views.contact, name="contact_us"),
    url(r'^videos', views.videos_page, name="videos"),
    url(r'^quiz', views.quiz_page, name="quiz"),
    url(r'^list_of_quiz', views.list_of_quiz, name="list_of_quiz"),
    url(r'^great_people', views.great_people, name="great_people"),
    url(r'^facts', views.facts, name="facts")
]
