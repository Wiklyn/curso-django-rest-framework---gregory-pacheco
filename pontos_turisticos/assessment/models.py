from django.contrib.auth.models import User
from django.db import models

class Assessment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  feedback = models.TextField(null=True, blank=True)
  rate = models.DecimalField(max_digits=3, decimal_places=2)
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user.username