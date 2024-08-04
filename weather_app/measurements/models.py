from django.db import models

class Measurement(models.Model):
    """
    Represents a weather measurement taken at a specific station and time.

    Attributes:
        timestamp (DateTimeField): The time when the measurement was taken.
        station_id (CharField): The identifier of the weather station where the measurement was recorded.
        temperature (FloatField): The temperature measured in degrees Celsius.
        humidity (FloatField): The humidity level measured in percentage.
        wind_speed (FloatField): The wind speed measured in meters per second.
        wind_direction (CharField): The direction of the wind, using cardinal directions (e.g., N, NE).
        rain_gauge (FloatField): The amount of rainfall measured in millimeters.
    """

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