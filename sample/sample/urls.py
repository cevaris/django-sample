from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from polls import views

urlpatterns = patterns('',
  
    url(r'^$', views.HomeView.as_view(), name='home'),

    url(r'^admin/', include(admin.site.urls)),

    # url(r'^polls/', include('polls.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
)