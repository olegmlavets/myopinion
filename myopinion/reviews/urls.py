from django.urls import path
from .views import TopicListCreateView, TopicRetrieveDestroyView

urlpatterns = [
    path('topic/', TopicListCreateView.as_view(), name='topic-list'),
    path('topic/<int:pk>/', TopicRetrieveDestroyView.as_view(), name='topic'),
]
