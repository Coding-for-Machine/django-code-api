from rest_framework import serializers
from .models import Unittestproblems, Memorytime

class UnittestproblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unittestproblems
        fields = '__all__'

class MemorytimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memorytime
        fields = '__all__'
