from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UnittestproblemsViewSet, MemorytimeViewSet, UnittestproblemsCreateAPIView

router = DefaultRouter()
router.register('test', UnittestproblemsViewSet)
router.register('memorytime', MemorytimeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API endpointlar uchun
    path('api/test/create/', UnittestproblemsCreateAPIView.as_view(), name='unittestproblems-create'),
]
