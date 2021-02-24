from rest_framework import viewsets

from .models import Topic
from .serializers import TopicSerializer, TopicDetailSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TopicDetailSerializer
        return TopicSerializer

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)
