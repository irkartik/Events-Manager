from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homeview, name='home'),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('create/', views.create, name="create_event"),
    path('<int:event_id>/delete', views.delete_event, name="delete_event"),
    path('<int:event_id>/update', views.update_event, name="update_event"),
    path('<int:event_id>/send_email', views.send_email, name="send_email"),
    
    path('show_users', views.show_users, name="show_users"),
    path('create_user', views.user_add, name="user_add"),
    path('<int:user_id>/delete_user', views.user_delete, name="user_delete"),
    #path('<int:user_id>/update_user', views.user_update, name="update_user"),
]