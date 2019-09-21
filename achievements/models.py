from django.db import models


class Achievement(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title + ' - ' + self.description
