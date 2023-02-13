from django.db import models
from attractions.models import Attraction
from feedback.models import Feedback
from assessment.models import Assessment
from addresses.models import Address

class Doc_ID(models.Model):
  id_description = models.CharField(max_length=100)

class PontoTuristico(models.Model):
  name = models.CharField(max_length=150)
  description = models.TextField()
  approved = models.BooleanField(default=False)
  attractions = models.ManyToManyField(Attraction)
  feedbacks = models.ManyToManyField(Feedback)
  assessment = models.ManyToManyField(Assessment)
  address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
  picture = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)
  doc_id = models.OneToOneField(Doc_ID, on_delete=models.CASCADE, null=True, blank=True)

  @property
  def full_description2(self):
    return f'{self.name} - {self.description}'

  def __str__(self):
    return self.name