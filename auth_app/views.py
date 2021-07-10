from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from auth_app.serializers import RegisterSerializer
from rest_framework.exceptions import ValidationError
from auth_app.models import User
from logging_config.logger import get_logger

# Logger configuration
logger = get_logger()


class RegisterAPIView(APIView):
    """
        RegisterAPIView: Create new user instance
    """
    def post(self, request):
        """
            This method is used to create new user instance.
            :param request: It's accept name, phone, email, property, service and message as parameter.
            :return: It's return response that user created successfully or not.
        """
        try:
            # Register serializer
            serializer = RegisterSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # Check given phone is already registered or not
            if User.objects.filter(phone=serializer.data.get('phone')).exists():
                return Response({'success': False, 'message': 'Gven phone number is already registered with another user.', 'data': {'phone': serializer.data.get('phone')}}, status=status.HTTP_400_BAD_REQUEST)
            # Check given email is already taken or not
            if User.objects.filter(email=serializer.data.get('email')).exists():
                return Response({'success': False, 'message': 'Gven email is already registered with another user.', 'data': {'email': serializer.data.get('email')}}, status=status.HTTP_400_BAD_REQUEST)
            # Register user
            user = User(name=serializer.data.get('name'), phone=serializer.data.get('phone'), email=serializer.data.get('email'), property=serializer.data.get('property'), service=serializer.data.get('service'), message=serializer.data.get('message'))
            # Save user
            user.save()
            # User registration successfull
            return Response({'success': True, 'message': 'Registration successfull!', 'data': {'email': serializer.data.get('email')}}, status=status.HTTP_200_OK)
        except ValidationError as e:
            logger.exception(e)
            return Response({'success': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False, 'message': 'Oops! Something went wrong! Please try again...'}, status=status.HTTP_400_BAD_REQUEST)
