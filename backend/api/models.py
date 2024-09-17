"""Models configuration for the Task model."""

from django.db import models


class Task(models.Model):
    """Configuration for the API models."""

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
