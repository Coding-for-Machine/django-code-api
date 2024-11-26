from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UnittestproblemsViewSet, MemorytimeViewSet

router = DefaultRouter()
router.register('unittestproblems', UnittestproblemsViewSet)
router.register('memorytime', MemorytimeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API endpointlar uchun
]
