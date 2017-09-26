from django.conf.urls import url
from nwhl_fantasy import views

urlpatterns = [url(r'^$', views.HomePageView.as_view()),]
