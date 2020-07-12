from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    portfolio = models.URLField(blank=False)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.name
