from django.db import models

# Create your models here.
class Ficheiros(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    resources = models.FileField(upload_to='resources/files')


    def __str__(self):
        return self.title
