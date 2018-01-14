from django.conf.urls import url
from nwhl_fantasy import views


#urlpatterns = [url(r'^$', views.HomePageView.as_view()),]
urlpatterns = [url(r'^$', views.index, name='index'),]
