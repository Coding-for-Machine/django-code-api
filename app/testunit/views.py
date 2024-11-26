from rest_framework import viewsets
from .models import Unittestproblems, Memorytime
from .serializers import UnittestproblemsSerializer, MemorytimeSerializer

class UnittestproblemsViewSet(viewsets.ModelViewSet):
    queryset = Unittestproblems.objects.all()
    serializer_class = UnittestproblemsSerializer

class MemorytimeViewSet(viewsets.ModelViewSet):
    queryset = Memorytime.objects.all()
    serializer_class = MemorytimeSerializer
