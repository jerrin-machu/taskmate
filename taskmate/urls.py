
from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_views
from userapp import views as userapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todolist_app.urls')),
    path('contact/', todolist_views.contact, name="contact"),
    path('about/', todolist_views.about, name="about"),
    path('', todolist_views.index, name="index"),
    path('accounts/', include('userapp.urls')),
   
]
