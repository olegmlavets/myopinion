from django.urls import path
from .views import TopicViewSet,ReviewViewSet

# /main
urlpatterns = [
    path('review/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'})),

    path('topic/', TopicViewSet.as_view({'get': 'list', 'post': 'create'}), name='topic-list-create'),
    path('topic/<int:pk>/', TopicViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}),
         name='topic-retrieve-delete'),
]
