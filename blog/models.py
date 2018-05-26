from django.db import models

class Blog(models.Model):
    naslov = models.CharField(max_length = 30)
    datum = models.DateField()
    image = models.ImageField(upload_to='images/')
    besedilo = models.TextField(max_length = 2000)

    def __str__(self):
        return self.naslov

    def povzetek(self):
        return self.besedilo[:100]
