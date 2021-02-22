from rest_framework import generics, views
from .models import Topic
from .serializers import TopicSerializer


class TopicListCreateView(generics.ListCreateAPIView, views.APIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
