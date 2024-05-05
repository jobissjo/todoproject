from typing import Iterable
from django.db import models
import uuid
from django.contrib.auth.models import User as DjangoUser


from django.utils import timezone

class ToDo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    status = models.BooleanField(default=False)
    complete_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Change to DateTimeField

    def __str__(self) -> str:
        return self.task

    def save(self, *args, **kwargs) -> None:
        if self.complete_date is not None and self.complete_date < timezone.now().date():
            raise ValueError("complete_date must be null or greater than or equal to created_at.")
        super().save(*args, **kwargs)