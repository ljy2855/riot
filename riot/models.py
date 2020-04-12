from django.db import models
from django.conf import settings
from django.utils import timezone

class sohwan(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    accountID = models.CharField(max_length=200)
    uid = models.CharField(max_length=200)
    update = models.DateTimeField(default = timezone.now)
    
    def save(self,id,accountID,name):
        self.name = name
        self.accountID = accountID
        self.id = id
        self.update = timezone.now

    def __str__(self) : 
        return self.name







