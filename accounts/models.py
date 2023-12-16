
from django.db import models

class Mijoz(models.Model):
    ism = models.CharField(max_length=255)
    nomer = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField( null=True, auto_now_add=True)
    comment = models.TextField(blank=True, null=True)

    # coment = models.CharField(max_length=100)
    # updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.ism
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

# Rest of your code
