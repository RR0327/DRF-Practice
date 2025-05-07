from django.urls import include, path
from rest_framework import routers
from .views import RRModelViewSet

router = routers.DefaultRouter()
router.register(r'rrmodel', RRModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
