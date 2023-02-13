from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication
from django.http import HttpResponse


class PontoTuristicoViewSet(ModelViewSet):
  serializer_class = PontoTuristicoSerializer
  filter_backends = [filters.SearchFilter]
  search_fields = ['name', 'description', '^address__line1']
  """ lookup_field = 'name' """
  """ permission_classes = [DjangoModelPermissions] """
  """ authentication_classes = [TokenAuthentication] """

  def get_queryset(self):
    id = self.request.query_params.get('id', None)
    name = self.request.query_params.get('name', None)
    description = self.request.query_params.get('description', None)
    queryset = PontoTuristico.objects.all()
    if id:
      queryset = PontoTuristico.objects.filter(pk=id)
    
    if name:
      queryset = queryset.filter(name__iexact=name)

    if description:
      queryset = queryset.filter(description__iexact=description)

    return queryset
  
  def list(self, request, *args, **kwargs):
    return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)
  
  def create(self, request, *args, **kwargs):
    return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)
  
  def destroy(self, request, *args, **kwargs):
    return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

  def retrieve(self, request, *args, **kwargs):
    return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

  def update(self, request, *args, **kwargs):
    return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

  def partial_update(self, request, *args, **kwargs):
    return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

  @action(methods=['get'], detail=True)
  def report(self, request, pk=None):
    pass

  @action(methods=['get'], detail=False)
  def test(self, request):
    pass

  @action(methods=['post'], detail=True)
  def associate_attractions(self, request, id):
    attractions = request.data['ids']
    ponto = PontoTuristico.objects.get(id=id)
    ponto.attractions.set(attractions)
    ponto.save()
    return HttpResponse('OK')
