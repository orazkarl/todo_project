from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.tasks.models import Task
from apps.tasks.api.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing task instances.
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['completed']
    ordering_fields = ['created_at', 'completed']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
