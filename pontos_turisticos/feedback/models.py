from django.contrib.auth.models import User
from django.db import models

class Feedback(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  feedback = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  approved = models.BooleanField(default=True)

  def __str__(self):
    return self.user.username
