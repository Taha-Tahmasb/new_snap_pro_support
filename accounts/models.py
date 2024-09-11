from django.db import models
from django.contrib.auth.models import User
from pro_service.models import Subscription, SubscriptionRestaurant


class ProUser(models.Model):
    is_pro = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(null=True, blank=True)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, blank=True, null=True)

    

    def __str__(self):
        return f"Pro User: ({self.user_name})"

class ProRestaurant(models.Model):
    name = models.CharField(max_length=100)
    is_pro = models.BooleanField(default=False)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(null=True, blank=True)
    subscription = models.ForeignKey(SubscriptionRestaurant, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Pro Restaurant: {self.name}"


class Suporter(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_suportet = models.BooleanField(default=False)