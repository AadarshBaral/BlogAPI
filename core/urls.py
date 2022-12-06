from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.post_view_create),
    path('edit/<int:pk>/',views.post_edit),
    path('register/',views.register),
   
]
