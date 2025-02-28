from django.urls import path
from .views import MeasurementListCreateView, MeasurementUpdateView

# URL patterns for the Measurements app
urlpatterns = [
    path('measurements/', MeasurementListCreateView.as_view(), name='measurement-list'),
    path('measurements/update/<str:station_id>/<str:timestamp>/', MeasurementUpdateView.as_view(), name='measurement-update'),
]
