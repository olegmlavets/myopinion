from rest_framework import serializers
from .models import Topic, Review, Criterion


class CriterionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criterion
        fields = ['title', 'points']


class ReviewSerializer(serializers.ModelSerializer):
    criterions = CriterionSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    def validate(self, attrs):
        if len(attrs.get('criterions', [])) > 3:
            raise serializers.ValidationError({"error": "No more than 3 criterion for review"})
        return attrs

    def create(self, validated_data):
        criterions_data: list = validated_data.pop('criterions', [])
        new_review: Review() = Review.objects.create(**validated_data)
        for item in criterions_data:
            CriterionSerializer(**item).save(review=new_review.id)
        return new_review

    class Meta:
        model = Review
        fields = ['title', 'advantages', 'disadvantages', 'text', 'updated_at', 'rating', 'criterions', 'on', 'author']


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
