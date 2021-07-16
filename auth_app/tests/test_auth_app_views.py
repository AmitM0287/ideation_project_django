import pytest
import json
from django.urls import reverse


class TestRegisterAPIView:
    """
        TestRegisterAPIView
    """
    @pytest.mark.django_db
    def test_response_as_registration_successful(self, client, django_user_model):
        # Url
        url = reverse('auth_app:user_register')
        # Registration succesfull
        data = {'name': 'Amit Manna', 'phone': '7896523145', 'email': 'amitmanna0287@gmail.com', 'property': 'property type 1', 'service': 'service type 1', 'message': 'good service'}
        response = client.post(url, data)
        # Verify status
        assert response.status_code == 200
        json_data = json.loads(response.content)
        # Verify response
        assert json_data['data']['email'] == 'amitmanna0287@gmail.com'

    # @pytest.mark.django_db
    # def test_response_as_given_email_is_already_register_with_another_user(self, client, django_user_model):
    #     # Create user
    #     user = django_user_model.objects.create_user(name='Minu Manna', phone='7852145639', email='amitmanna0287@gmail.com', property='property type 2', service='service type 1', message='good')
    #     user.save()
    #     # Url
    #     url = reverse('auth_app:user_register')
    #     # Email is already exist
    #     data = {'name': 'Amit Manna', 'phone': '7896523145', 'email': 'amitmanna0287@gmail.com', 'property': 'property type 1', 'service': 'service type 1', 'message': 'good service'}
    #     response = client.post(url, data)
    #     # Verify status
    #     assert response.status_code == 400
