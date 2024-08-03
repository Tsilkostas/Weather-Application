from rest_framework import generics
from .models import Measurement
from .serializers import MeasurementSerializer
from django.utils.dateparse import parse_datetime
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import Http404
from rest_framework.exceptions import ValidationError

class MeasurementListCreateView(generics.ListCreateAPIView):
    serializer_class = MeasurementSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
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
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    
    def get_object(self):
        # Fetch object based on timestamp and station_id
        timestamp = self.kwargs['timestamp']
        station_id = self.kwargs['station_id']
        try:
            return Measurement.objects.get(timestamp=timestamp, station_id=station_id)
        except Measurement.DoesNotExist:
            raise Http404("Measurement not found.")



