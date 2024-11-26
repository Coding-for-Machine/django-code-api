from rest_framework import serializers
from .models import Problems
from rest_framework import serializers
from .models import Language, Category, Tage, Problems, Answer, Comments, Algorithm

class ProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problems
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # If the 'body' contains media URLs, replace them with the full URL
        if 'body' in data:
            data['body'] = self.make_absolute_urls(data['body'])

        return data

    def make_absolute_urls(self, body):
        if body:
            # Get the full media URL using the request object
            body = body.replace('/media/', f'{self.context["request"].build_absolute_uri("/media/")}')
        return body
    
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tage
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class AlgorithmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Algorithm
        fields = '__all__'

