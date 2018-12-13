from django.db import models
from django.utils import timezone

from .tasks import create_user


class Rant(models.Model):
    text = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        create_user.apply_async(
            eta=(timezone.now() + timezone.timedelta(seconds=15))
        )
        return super().save(*args, **kwargs)
