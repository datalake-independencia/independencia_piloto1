from django.db import models
#from s3direct.fields import S3DirectField

# Create your models here.


class files(models.Model):

    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(max_length=1000, blank=False, null=False)
    file = models.FileField()
    #file = S3DirectField(dest='primary_destination')

    def __str__(self):
        return f"Archivo: {self.name}\n Descripción: {self.description[:100]}"
