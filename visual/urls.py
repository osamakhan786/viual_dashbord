from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from visual.views import VisualViewSet

router = routers.DefaultRouter()
router.register(r'', VisualViewSet)

urlpatterns = [
    path('',include(router.urls))
    
]
