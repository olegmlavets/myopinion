from django.urls import path
from .views import TopicListCreateView

urlpatterns = [
    path('topic/', TopicListCreateView.as_view(), name='topic')

]
