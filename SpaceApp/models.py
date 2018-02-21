from django.db import models


# Create your models here

class MsgFromSpace(models.Model):
    def __str__(self):
        return self.text + ' (' + str(self.date) + ')'

    date = models.DateField(blank=False)
    text = models.TextField(blank=False)
    read = models.BooleanField(default=False)
