from rest_framework.serializers import ModelSerializer, SerializerMethodField
from core.models import PontoTuristico, Attraction, Doc_ID
from attractions.api.serializers import AttractionSerializer
from addresses.api.serializers import AddressSerializer
from addresses.models import Address

class Doc_IDSerializer(ModelSerializer):
  class Meta:
    model = Doc_ID
    fields = '__all__'

class PontoTuristicoSerializer(ModelSerializer):
  attractions = AttractionSerializer(many=True)
  address = AddressSerializer(read_only=True)
  full_description = SerializerMethodField()
  doc_id = Doc_IDSerializer()

  def get_full_description(self, obj):
    return f'{obj.name} - {obj.description}'

  class Meta:
    model = PontoTuristico
    fields = ('id', 'name', 'description', 'approved', 'picture',
    'attractions', 'feedbacks', 'assessment', 'address',
    'full_description', 'full_description2', 'doc_id')
    read_only_fields = ('feedbacks', 'assessment')
  
  def create_attractions(self, attractions, ponto):
    for attracion in attractions:
      at = Attraction.objects.create(**attracion)
      ponto.attractions.add(at)

  def create(self, validated_data):
    attractions = validated_data['attractions']
    del validated_data['attractions']

    address = validated_data['address']
    del validated_data['address']

    doc = validated_data['doc_id']
    del validated_data['doc_id']
    doci = Doc_ID.objects.create('doc')

    ponto = PontoTuristico.objects.create(**validated_data)
    self.create_attractions(attractions, ponto)

    adr = Address.objects.create(**address)
    ponto.address = adr
    ponto.doc_id = doci

    ponto.save()

    return ponto
