from django.contrib.auth.models import User, Permission
from django.db import models

# Create your models here.

class Customer(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    customerPhone = models.CharField(max_length=15, unique=True)
    customerEmail = models.EmailField(unique=True)
    userName = models.ForeignKey(User , on_delete=models.CASCADE , related_name='customer')
    isActive = models.BooleanField(default=True)
    def __str__(self):
        return self.firstName + " "+ self.lastName



    # class Meta:
    #     permission = Permission.objects.create(
    #         codename='can_publish',
    #         name='Can Publish Posts',
    #         content_type=content_type,
    #     )



