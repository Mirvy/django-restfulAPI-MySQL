from django.conf.urls import url
from tasks import views

urlpatterns = [
    url(r'^api/tasks$', views.task_list),
    url(r'^api/tasks/(?P<pk>[0-9]+)$',views.task_detail),
    url(r'^api/tasks/urgent$',views.task_list_urgent),
    url(r'^api/clients$', views.client_list),
    url(r'^api/clients/(?P<pk>[0-9]+)$',views.client_detail)
]