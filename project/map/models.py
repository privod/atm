from django.db import models


class Atm(models.Model):
    ref = models.IntegerField(primary_key=True)
    serial = models.CharField()
    number = models.CharField()
    producer = models.CharField()
    model = models.CharField()
    city = models.CharField()
    address = models.CharField()

    def __str__(self):
        return '{}: {}'.format(self.producer, self.serial)