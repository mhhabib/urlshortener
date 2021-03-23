from django.db import models

# Create your models here.


class Url(models.Model):
    link = models.CharField(max_length=10000, blank=False)
    uuid = models.CharField(max_length=10)

    def __str__(self):
        return self.link[:40]+" - "+self.uuid
