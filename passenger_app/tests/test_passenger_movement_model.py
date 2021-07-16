import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestPassengerMovementModel:
    """
        TestPassengerMovementModel : Testing Passenger Movement Model
    """
    def test_init(self):
        passenger_obj = mixer.blend('passenger_app.passenger_movement')
        assert passenger_obj.id >= 1, 'should save an instance'
