from django.contrib import admin

from apps.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "completed", "created_at", "user")
    list_filter = ("completed",)
    search_fields = ("title", "description")
