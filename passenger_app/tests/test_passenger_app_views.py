import pytest
from django.urls import reverse

class TestPassengerAPIView:
    """
        TestPassengerAPIView
    """
    @pytest.mark.django_db
    def test_response_as_all_data_stored_successfully(self, client, django_user_model):
        url = reverse('passenger_app:passenger_data')
        with open('data/TS Total passenger movements.csv') as fp:
            response = client.post(url, {'file': fp})
        assert response.status_code == 200
    
    @pytest.mark.django_db
    def test_response_while_getting_all_data_as_something_went_wrong(self, client, django_user_model):
        url = reverse('passenger_app:passenger_data')
        data = { 
            "page_no": 10
        }
        response = client.get(url, data)
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_response_as_getting_all_data_successfully(self, client, django_user_model):
        url = reverse('passenger_app:passenger_data')
        with open('data/TS Total passenger movements.csv') as fp:
            response = client.post(url, {'file': fp})
        url = '/passenger/data/?page_no=10'
        response = client.get(url)
        assert response.status_code == 200
