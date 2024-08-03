from django.db import models

class Measurement(models.Model):
    timestamp = models.DateTimeField()
    station_id = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    wind_direction = models.CharField(max_length=10)
    rain_gauge = models.FloatField()
    
    class Meta:
        unique_together = ('timestamp', 'station_id')

    def __str__(self):
        return f'{self.station_id} at {self.timestamp}'