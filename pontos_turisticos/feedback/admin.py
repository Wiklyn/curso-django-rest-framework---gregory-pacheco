from django.contrib import admin
from .models import Feedback
from .actions import reprove_feedbacks, approve_feedbacks

class FeedbackAdmin(admin.ModelAdmin):
  list_display = ['user', 'date', 'approved']
  actions = [reprove_feedbacks, approve_feedbacks]

admin.site.register(Feedback, FeedbackAdmin)
