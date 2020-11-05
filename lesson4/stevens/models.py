from django.db import models

# Create your models here.
class TemperatureData(models.Model):
    date_time = models.CharField(max_length=30)
    temperature = models.CharField(max_length=5)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    def __str__(self):
        """
        Returns the string representation of the date.

        Args:
            self: (todo): write your description
        """
        return self.date_time
