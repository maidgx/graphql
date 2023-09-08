from django.db import models

class Number(models.Model):
    value = models.IntegerField()

    def __int__(self):
        return self.value

