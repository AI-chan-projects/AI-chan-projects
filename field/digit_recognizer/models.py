from django.db import models

# Create your models here.
class DigitRecognizer(models.Model):
    #필드 정의
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name