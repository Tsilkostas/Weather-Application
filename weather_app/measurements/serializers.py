from rest_framework import serializers
from .models import Measurement

class MeasurementSerializer(serializers.ModelSerializer):
    """
    Serializer for the Measurement model.

    This serializer handles validation and serialization for the Measurement model, 
    ensuring that data is correctly formatted and adheres to specific constraints 
    before being processed or saved.
    """
    class Meta:
        model = Measurement
        fields = '__all__'

    def validate(self, data):
        """
        Validate the data for uniqueness and other custom rules.

        This method ensures that the combination of timestamp and station_id is unique,
        which prevents duplicate entries for the same station at the same time.

        """
        instance = self.instance
        if instance and Measurement.objects.filter(
                timestamp=data['timestamp'], 
                station_id=data['station_id']
            ).exclude(id=instance.id).exists():
            raise serializers.ValidationError("The combination of timestamp and station_id must be unique.")
        return data

    def validate_temperature(self, value):
        """
        Validate the temperature value.

        Ensures that the temperature is within the acceptable range of -50°C to 60°C.

        """
        if not (-50 <= value <= 60):
            raise serializers.ValidationError("The temperature must be between -50°C and 60°C.")
        return value

    def validate_humidity(self, value):
        """
        Validate the humidity value.

        Ensures that the humidity is within the acceptable range of 0% to 100%.

        """
        if not (0 <= value <= 100):
            raise serializers.ValidationError("The humidity must be between 0%  and 100%.")
        return value
    
    def validate_wind_speed(self, value):
        """
        Validate the wind speed value.

        Ensures that the wind speed is within the acceptable range of 0 m/s to 100 m/s.

        """
        if not (0 <= value <= 100):
            raise serializers.ValidationError("The wind speed must be between 0 m/s and 100 m/s.")
        return value

    def validate_wind_direction(self, value):
        """
        Validate the wind direction value.

        Ensures that the wind direction is one of the valid cardinal directions.

        """
        valid_directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        if value not in valid_directions:
            raise serializers.ValidationError(f"The direction of the wind should be one of the following: {', '.join(valid_directions)}.")
        return value

    def validate_rain_gauge(self, value):
        """
        Validate the rain gauge value.

        Ensures that the rain gauge measurement is zero or a positive value.

        """
        if value < 0:
            raise serializers.ValidationError("The rain gauge measurements must be zero or positive values.")
        return value