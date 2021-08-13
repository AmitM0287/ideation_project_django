from rest_framework import serializers
from passenger_app.models import passenger_movement


class PassengerMovementSerializer(serializers.Serializer):
    """
        PassengerMovementSerializer: Date, ArrivalsActualCounts, DeparturesActualCounts
    """
    Date = serializers.DateTimeField()
    ArrivalsActualCounts = serializers.IntegerField()
    DeparturesActualCounts = serializers.IntegerField()

    class Meta:
        model = passenger_movement
        fields = ['Date', 'ArrivalsActualCounts', 'DeparturesActualCounts']
