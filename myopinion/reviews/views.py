from rest_framework import viewsets, mixins, exceptions, generics, views
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Topic, Review
from .serializers import TopicSerializer, TopicDetailSerializer, ReviewSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TopicDetailSerializer
        return TopicSerializer

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
