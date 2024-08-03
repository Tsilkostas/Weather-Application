from rest_framework import serializers
from .models import Measurement

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'

    def validate(self, data):
        instance = self.instance
        if instance and Measurement.objects.filter(
                timestamp=data['timestamp'], 
                station_id=data['station_id']
            ).exclude(id=instance.id).exists():
            raise serializers.ValidationError("The combination of timestamp and station_id must be unique.")
        return data

    def validate_temperature(self, value):
        if not (-50 <= value <= 60):
            raise serializers.ValidationError("The temperature must be between -50°C and 60°C.")
        return value

    def validate_humidity(self, value):
        if not (0 <= value <= 100):
            raise serializers.ValidationError("The humidity must be between 0%  and 100%.")
        return value
    
    def validate_wind_speed(self, value):
        if not (0 <= value <= 100):
            raise serializers.ValidationError("The wind speed must be between 0 m/s and 100 m/s.")
        return value

    def validate_wind_direction(self, value):
        valid_directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        if value not in valid_directions:
            raise serializers.ValidationError(f"The direction of the wind should be one of the following: {', '.join(valid_directions)}.")
        return value

    def validate_rain_gauge(self, value):
        if value < 0:
            raise serializers.ValidationError("The rain gauge measurements must be zero or positive values.")
        return value