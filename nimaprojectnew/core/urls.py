from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homeview, name='home'),
    url(r'^login/$', views.login_user, name="login_user"),
    url(r'^logout/$', views.logout_user, name="logout"),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^create/$', views.create, name="create_event"),
    url(r'^event/(?P<event_id>[0-9])/$', views.event_page, name="event_page"),
    url(r'^(?P<event_id>[0-9])/delete/$', views.delete_event, name="delete_event"),
    url(r'^(?P<event_id>[0-9])/update/$', views.update_event, name="update_event"),
    url(r'^(?P<event_id>[0-9])/send_email/$', views.send_email, name="send_email"),

    url(r'^show_users/$', views.show_users, name="show_users"),
    url(r'^create_user/$', views.user_add, name="user_add"),
    url(r'^(?P<user_id>[0-9])/delete_user/$', views.user_delete, name="user_delete"),
    #path('<int:user_id>/update_user', views.user_update, name="update_user"),

]