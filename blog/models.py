from django.db import models

class Blog(models.Model):
    naslov = models.CharField(max_length = 30)
    datum = models.DateField()
    image = models.ImageField(upload_to='images/')
    besedilo = models.CharField(max_length = 2000)
