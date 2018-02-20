"""nimaprojectnew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from core import views as coreviews
from userdata import views as userdataviews
from . import settings
from django.conf.urls.static import static



router = routers.DefaultRouter()
router.register(r'api/users', coreviews.UserViewSet)
router.register(r'api/events', coreviews.EventViewSet)
router.register(r'api/appointments', userdataviews.AppointmentViewSet)
router.register(r'api/eligibility', userdataviews.EligibilityViewSet)
router.register(r'api/appliedusers', userdataviews.AppliedUserViewSet)

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^', include('userdata.urls')),
	url(r'^', include('core.urls')),
	url(r'^', include(router.urls)),
	url(r'^api-auth', include('rest_framework.urls'), name='rest_framework'),
	#url(r'appointment/(?P<movie_id>.+)/', views.AppointmentIndivisual.as_view()),
	url(r'^api/appointments/(?P<appointment_id>[0-9])', userdataviews.AppointmentIndivisual.as_view()),
	url(r'^api/appliedusers/(?P<applieduser_id>[0-9])', userdataviews.AppliedUserIndivisual.as_view()),
	url(r'^api/eligibility/(?P<eligibility_id>[0-9])', userdataviews.EligibilityIndivisual.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
