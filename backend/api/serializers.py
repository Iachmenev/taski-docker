"""Serializers configuration for the Task model."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Configuration for the API serializers."""

    class Meta:
        """Meta class for TaskSerializer."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
