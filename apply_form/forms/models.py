from django.db import models

# Create your models here.
class ApllyContent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=99)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name
