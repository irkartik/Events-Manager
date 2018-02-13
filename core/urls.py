from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('create/', views.create, name="create_event"),
    path('<int:event_id>/delete', views.delete_event, name="delete_event"),
    path('<int:event_id>/update', views.update_event, name="update_event"),
]