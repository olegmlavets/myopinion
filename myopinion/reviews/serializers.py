from rest_framework import serializers
from .models import Topic, Review, Criterion


class CriterionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criterion
        fields = ['title', 'points']


class ReviewSerializer(serializers.ModelSerializer):
    criterions = CriterionSerializer(many=True, allow_null=True)

    class Meta:
        model = Review
        fields = ['title', 'advantages', 'disadvantages', 'text', 'updated_at', 'rating', 'criterions']


class TopicSerializer(serializers.ModelSerializer):
    topic_rating = serializers.FloatField(source='rating', read_only=True)
    creator = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Topic
        fields = ['title', 'creator', 'topic_rating', 'created_at', ]


class TopicDetailSerializer(TopicSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ['title', 'creator', 'topic_rating', 'created_at', 'reviews', ]

# class TopicDetailSerializer(serializers.ModelSerializer):
#     topic_rating = serializers.FloatField(source='rating', read_only=True)
#     creator = serializers.StringRelatedField(read_only=True)
#     reviews = ReviewSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Topic
#         fields = ['title', 'creator', 'topic_rating', 'created_at', 'reviews', ]
