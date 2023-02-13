def reprove_feedbacks(modeladmin, request, queryset):
  queryset.update(approved=False)


def approve_feedbacks(modeladmin, request, queryset):
  queryset.update(approved=False)

reprove_feedbacks.short_description = "Reprovar comentários"
approve_feedbacks.short_description = "Aprovar comentários"
