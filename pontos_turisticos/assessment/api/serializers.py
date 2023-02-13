from rest_framework.serializers import ModelSerializer
from assessment.models import Assessment

class AssessmentSerializer(ModelSerializer):
  class Meta:
    model = Assessment
    fields = ('id', 'user', 'feedback', 'rate', 'date')