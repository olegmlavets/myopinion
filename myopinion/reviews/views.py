from rest_framework import generics, views
from .models import Topic
from .serializers import TopicSerializer


class TopicListCreateView(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)


class TopicRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
