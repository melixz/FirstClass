from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'number', 'email', 'time_created')
    list_filter = ('id', 'full_name', 'number', 'email', 'time_created')
    search_fields = ('id', 'full_name', 'number', 'email', 'time_created')
    ordering = ('id', 'full_name', 'number', 'email', 'time_created')


admin.site.register(Feedback)
