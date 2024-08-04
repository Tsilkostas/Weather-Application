from rest_framework import generics
from .models import Measurement
from .serializers import MeasurementSerializer
from django.utils.dateparse import parse_datetime
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import Http404
from rest_framework.exceptions import ValidationError

class MeasurementListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating Measurement records.

    This view supports retrieving a list of Measurement records based on optional filters,
    and creating new Measurement records. Filters include date range (from/to) and station IDs.
    """
    serializer_class = MeasurementSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        """
        Retrieve the queryset of Measurement records.

        This method filters the Measurement records based on the query parameters
        provided in the request. The supported filters are:
        - 'date_from': The start date for the range filter.
        - 'date_to': The end date for the range filter.
        - 'station_ids': A list of station IDs to filter by.

        Returns:
            QuerySet: A queryset of Measurement records filtered by the specified parameters.

        Raises:
            ValidationError: If the date_from or date_to query parameters are not valid datetime strings.
        """
        queryset = Measurement.objects.all()
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)
        station_ids = self.request.query_params.getlist('station_ids', None)

        if date_from:
            date_from = parse_datetime(date_from)
            if date_from is None:
                raise ValidationError("Invalid 'date_from' format.")
            queryset = queryset.filter(timestamp__gte=date_from)
        if date_to:
            date_to = parse_datetime(date_to)
            if date_to is None:
                raise ValidationError("Invalid 'date_to' format.")
            queryset = queryset.filter(timestamp__lte=date_to)
        
        if station_ids:
            queryset = queryset.filter(station_id__in=station_ids)

        return queryset

class MeasurementUpdateView(generics.UpdateAPIView):
    """
    API view for updating a specific Measurement record.

    This view allows for the updating of a Measurement record identified by a 
    combination of 'timestamp' and 'station_id' in the URL.
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    def get_object(self):
        """
        Retrieve a specific Measurement record.

        This method fetches a Measurement record based on the 'timestamp' and 
        'station_id' provided in the URL. If no such record exists, it raises a 404 error.

        Returns:
            Measurement: The Measurement instance that matches the provided 'timestamp' and 'station_id'.

        Raises:
            Http404: If no Measurement record is found with the given 'timestamp' and 'station_id'.
        """
        timestamp = self.kwargs['timestamp']
        station_id = self.kwargs['station_id']
        try:
            return Measurement.objects.get(timestamp=timestamp, station_id=station_id)
        except Measurement.DoesNotExist:
            raise Http404("Measurement not found.")



