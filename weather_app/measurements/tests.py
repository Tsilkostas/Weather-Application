from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Measurement
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


class MeasurementAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        
        # Create a user and obtain a JWT token
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        
        self.measurement_data = {
            'timestamp': '2024-01-01T00:00:00Z',
            'station_id': 'Station1',
            'temperature': 25.0,
            'humidity': 50.0,
            'wind_speed': 5.0,
            'wind_direction': 'N',
            'rain_gauge': 0.0
        }
        # Create initial data
        Measurement.objects.create(**self.measurement_data)

    def test_list_measurements(self):
        response = self.client.get('/api/measurements/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0, "No measurements found in the list")

    def test_create_measurement(self):
        # Ensure the data being created is unique by modifying the timestamp or station_id
        unique_measurement_data = self.measurement_data.copy()
        unique_measurement_data['timestamp'] = '2024-01-01T01:00:00Z'  # Change timestamp for uniqueness

        response = self.client.post('/api/measurements/', unique_measurement_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['station_id'], unique_measurement_data['station_id'])
        self.assertEqual(response.data['temperature'], unique_measurement_data['temperature'])


    def test_update_measurement(self):
        # Full data including all required fields
        update_data = {
            'timestamp': '2024-01-01T00:00:00Z',
            'station_id': 'Station1',
            'temperature': 30.0,  # The field we are updating
            'humidity': 50.0,
            'wind_speed': 5.0,
            'wind_direction': 'N',
            'rain_gauge': 0.0
        }
        
        # Assuming the measurement already exists from setUp
        response = self.client.put('/api/measurements/update/Station1/2024-01-01T00:00:00Z/', update_data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify that the update was successful
        updated_measurement = Measurement.objects.get(timestamp='2024-01-01T00:00:00Z', station_id='Station1')
        self.assertEqual(updated_measurement.temperature, 30.0)




    def test_create_measurement_invalid_data(self):
        invalid_data = self.measurement_data.copy()
        invalid_data['temperature'] = 1000.0  # Invalid temperature
        response = self.client.post('/api/measurements/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_measurement_not_found(self):
        update_data = {'temperature': 30.0}
        response = self.client.put('/api/measurements/update/NonExistentStation/2024-01-01T00:00:00Z/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


