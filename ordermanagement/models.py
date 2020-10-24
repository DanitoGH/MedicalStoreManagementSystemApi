from django.db import models
from django.utils import timezone
from stockmanagement.models import AddStockItem
from clientsmanagement.models import Client


class CreateOrder(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(AddStockItem, on_delete=models.DO_NOTHING)
    ordered_qty = models.DecimalField(max_digits=6, decimal_places=0)
    delivered_qty = models.DecimalField(max_digits=6, decimal_places=0)
    unit = models.CharField(max_length=100, blank=True, null=True, default='')
    urgency_level = models.CharField(max_length=30, blank=False, null=False, default='Normal')
    date_ordered = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, blank=False, null=False, default='Pending')
    objects = models.Manager()

    class Meta:
        ordering = ['-date_ordered']

    def __str__(self):
        return self.item.name