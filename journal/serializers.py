
from rest_framework import serializers
from .models import Mood, Category, JournalEntry

class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class JournalEntrySerializer(serializers.ModelSerializer):
    mood_name = serializers.StringRelatedField(source='mood', read_only=True)
    category_name = serializers.StringRelatedField(source='category', read_only=True)

    class Meta:
        model = JournalEntry
        fields = '__all__'
        read_only_fields = ['user']
