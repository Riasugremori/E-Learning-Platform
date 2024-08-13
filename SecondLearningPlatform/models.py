from django.db import models
from django.contrib.auth.models import User

class EnteredText(models.Model):
    entered_url = models.CharField(max_length=100)

    def __str__(self):
        return self.entered_url
    
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_instructor = models.BooleanField(default=False)
