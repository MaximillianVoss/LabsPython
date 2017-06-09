from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

router = routers.DefaultRouter()

urlpatterns = {
    #url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?MyProject<question_id>[0-9]+)/$', detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?MyProject<question_id>[0-9]+)/results/$', results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?MyProject<question_id>[0-9]+)/vote/$', vote, name='vote'),

    url(r'^home/$', 'todolist.views.Login'),
    url(r'^tags/$', TagCreateView.as_view(), name='tags-list'),
    url(r'^users/$', UserCreateView.as_view(), name="user-list"),
    url(r'^todolists/$', TasklistCreateView.as_view(), name="lists"),
    url(r'^todolists/(?MyProject<pk>[0-9]+)/$', TasklistDetailsView.as_view(), name="list-detail"),
    url(r'^todolists/(?MyProject<list_id>[0-9]+)/tasks', TaskCreateView.as_view(), name="list-create"),
    url(r'^todolists/(?MyProject<list_id>[0-9]+)/tasks/(?MyProject<pk>[0-9]+)', TaskDetailsView.as_view(), name="detail"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
