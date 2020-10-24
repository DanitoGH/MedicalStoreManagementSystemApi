from django.db import models
from django.utils import timezone
from account.models import Account


class ActivityTracker(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    activity = models.CharField(max_length=120, blank=False, null=False)
    activity_type = models.CharField(max_length=16, blank=False, null=False, default='General')
    activity_date = models.DateTimeField(default=timezone.now)
    objects = models.Manager()

    class Meta:
        ordering = ['-activity_date']

    def __str__(self):
        return self.activity
 