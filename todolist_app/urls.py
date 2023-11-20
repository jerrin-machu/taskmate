from django.urls import path
from todolist_app import views


urlpatterns = [
    path('', views.todolist, name='todolist'),
    
    path('delete/<taskid>',views.delete_task,name='delete_task'),
    path('edit/<taskid>', views.edit_task, name='edit_task'),
    path('complete/<taskid>', views.complete_task, name='complete_task'),
    path('pending/<taskid>', views.pending_task, name='pending_task')
    
]