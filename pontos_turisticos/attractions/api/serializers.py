from rest_framework.serializers import ModelSerializer
from attractions.models import Attraction

class AttractionSerializer(ModelSerializer):
  class Meta:
    model = Attraction
    fields = ('id', 'name', 'description', 'opening_hours', 'minimum_age', 'picture')