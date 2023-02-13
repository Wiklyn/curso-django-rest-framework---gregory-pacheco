from rest_framework.serializers import ModelSerializer
from feedback.models import Feedback

class FeedbackSerializer(ModelSerializer):
  class Meta:
    model = Feedback
    fields = ('id', 'user', 'feedback', 'date', 'approved')