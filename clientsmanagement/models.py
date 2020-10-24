from django.db import models

from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_delete

from stockmanagement.models import AddStockItem
from account.models import Account



def upload_location(instance, filename):
    file_path = 'profile_images/{user_id}/{hospital_name}-{filename}'.format(
        user_id=str(instance.user.id), hospital_name=str(instance.hospital_name), filename=filename
    )
    return file_path


class Client(models.Model):
    user = models.OneToOneField(Account, null=False, blank=False, on_delete=models.CASCADE, default='null')
    hospital_name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    location = models.CharField(max_length=200, blank=False, null=False, default='Not available')
    phone = models.CharField(max_length=60, default='Not available')
    profile_photo = models.ImageField(upload_to=upload_location, blank=True, null=True)
    status = models.CharField(max_length=30, blank=False, null=False, default='active')
    date_joined = models.DateTimeField(default=timezone.now)
    objects = models.Manager()
    
    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return self.hospital_name


@receiver(post_delete, sender=Client)
def submission_delete(sender, instance, **kwargs):
    instance.profile_photo.delete(True)