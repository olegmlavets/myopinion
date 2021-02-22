from rest_framework import serializers
from .models import Topic


class TopicSerializer(serializers.ModelSerializer):
    topic_rating = serializers.FloatField(source='rating', read_only=True)

    class Meta:
        model = Topic
        fields = ['title', 'topic_rating', 'created_at', 'updated_at']
