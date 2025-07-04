from django.urls import path,include
from rest_framework.routers import DefaultRouter
from.views import VitalSignsViewSet

router=DefaultRouter()
router.register('vitalsigns',VitalSignsViewSet)
urlpatterns = [
    path('',include(router.urls)),
]
