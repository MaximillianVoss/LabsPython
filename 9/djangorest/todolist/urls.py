from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TaskCreateView, TaskDetailsView, TasklistCreateView, TasklistDetailsView, TagCreateView, \
    TagDetailsView, \
    UserCreateView, UserDetailsView

router = routers.DefaultRouter()

router.register(r'tagtypes', TagDetailsView)
router.register(r'tags', TagCreateView)


urlpatterns = {
    url(r'^todolists/users/$', UserDetailsView.as_view({'get': 'list'}), name="users"),
    url(r'^todolists/$', TasklistCreateView.as_view(), name="lists"),
    url(r'^todolists/(?P<pk>[0-9]+)/$', TasklistDetailsView.as_view(), name="list-detail"),
    url(r'^todolists/(?P<list_id>[0-9]+)/tasks', TaskCreateView.as_view(), name="tasks"),
    url(r'^todolists/(?P<list_id>[0-9]+)/tasks/(?P<pk>[0-9]+)', TaskDetailsView.as_view(), name="task-detail"),
}

urlpatterns = format_suffix_patterns(urlpatterns)