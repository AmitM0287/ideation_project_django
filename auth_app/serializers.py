from rest_framework import serializers
from auth_app.models import User

class RegisterSerializer(serializers.ModelSerializer):
    """
        Register Serializer : first_name, last_name, email, username, password
    """
    name = serializers.CharField(min_length=2, max_length=60, required=True)
    phone = serializers.CharField(min_length=10, max_length=12,required=True)
    email = serializers.EmailField(min_length=4, max_length=60, required=True)
    property = serializers.CharField(min_length=2, max_length=60, required=True)
    service = serializers.CharField(min_length=2, max_length=60, required=True)
    message = serializers.CharField(min_length=2, max_length=150, required=True)

    class Meta:
        model = User
        fields = ['name', 'phone', 'email', 'property', 'service', 'message']
