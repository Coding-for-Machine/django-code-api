from rest_framework import viewsets
from .models import Language, Category, Tage, Problems, Answer, Comments, Algorithm
from .serializers import (
    LanguageSerializer, CategorySerializer, TageSerializer,
    ProblemsSerializer, AnswerSerializer, CommentsSerializer, AlgorithmSerializer
)

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TageViewSet(viewsets.ModelViewSet):
    queryset = Tage.objects.all()
    serializer_class = TageSerializer

class ProblemsViewSet(viewsets.ModelViewSet):
    queryset = Problems.published.all()  # Faqat faollashtirilgan muammolarni olish
    serializer_class = ProblemsSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.filter(active=True)  # Faqat faol izohlarni olish
    serializer_class = CommentsSerializer

class AlgorithmViewSet(viewsets.ModelViewSet):
    queryset = Algorithm.objects.filter(active=True)  # Faqat faol algoritmlarni olish
    serializer_class = AlgorithmSerializer
