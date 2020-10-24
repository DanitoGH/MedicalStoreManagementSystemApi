from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete

from stockmanagement.models import AddStockItem
from account.models import Account


def upload_location(instance, filename):
    file_path = 'profile_images/{user_id}/{username}-{filename}'.format(
        user_id=str(instance.user.id), username=str(instance.user.username), filename=filename
    )
    return file_path


class OperationsAdminProfile(models.Model):
    user = models.OneToOneField(Account, null=False, blank=False, on_delete=models.CASCADE, default='null')
    phone = models.CharField(max_length=60)
    profile_photo = models.ImageField(upload_to=upload_location, blank=True, null=True)
    status = models.CharField(max_length=30, blank=False, null=False, default='active')
    objects = models.Manager()

    def __str__(self):
        return self.user.username


@receiver(post_delete, sender=OperationsAdminProfile)
def submission_delete(sender, instance, **kwargs):
    instance.profile_photo.delete(True)