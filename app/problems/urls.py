from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    LanguageViewSet, CategoryViewSet, TageViewSet, ProblemsViewSet,
    AnswerViewSet, CommentsViewSet, AlgorithmViewSet
)

router = DefaultRouter()
router.register('languages', LanguageViewSet)
router.register('categories', CategoryViewSet)
router.register('tags', TageViewSet)
router.register('problems', ProblemsViewSet)
router.register('answers', AnswerViewSet)
router.register('comments', CommentsViewSet)
router.register('algorithms', AlgorithmViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API barcha endpointlari
]
