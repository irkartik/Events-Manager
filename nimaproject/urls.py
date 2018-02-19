"""nimaproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

from rest_framework import routers
from core import views as coreviews
from userdata import views as userdataviews

router = routers.DefaultRouter()
router.register(r'api/users', coreviews.UserViewSet)
router.register(r'api/events', coreviews.EventViewSet)
router.register(r'api/appointments', userdataviews.AppointmentViewSet)
router.register(r'api/eligibility', userdataviews.EligibilityViewSet)
router.register(r'api/appliedusers', userdataviews.AppliedUserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('userdata.urls')),
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls'), name='rest_framework'),
    #url(r'appointment/(?P<movie_id>.+)/', views.AppointmentIndivisual.as_view()),
    path('api/appointments/<int:appointment_id>', userdataviews.AppointmentIndivisual.as_view()),
    path('api/appliedusers/<int:applieduser_id>', userdataviews.AppliedUserIndivisual.as_view()),
    path('api/eligibility/<int:eligibility_id>', userdataviews.EligibilityIndivisual.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)