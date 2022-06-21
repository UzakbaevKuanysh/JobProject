from django.urls import path, re_path

from rest_framework.urlpatterns import format_suffix_patterns
from main import views
from main.views import WorkerViewSet, WorkerViewSet_detail, add_worker, delete_worker, edit_worker, index, register, update_worker

app_name = 'main'

workers = WorkerViewSet.as_view({
  'get': 'list',
  'post': 'create'
})
workers_detail = WorkerViewSet_detail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    
})

urlpatterns = [
  path('', index , name ="index"),
  path('worker/', workers, name = "workers"),
  path('worker/<int:pk>/', workers_detail, name = "workers"),
  path('accounts/register/', register, name = 'register'),
  path('add_worker', add_worker, name='add_worker'),
  path('delete_worker/<int:myid>/', delete_worker, name = "delete_worker"),
  path('edit_worker/<int:myid>/', edit_worker, name = "edit_worker"),
  path('update_worker/<int:myid>/', update_worker, name = "update_worker")
  ]
urlpatterns = format_suffix_patterns(urlpatterns)