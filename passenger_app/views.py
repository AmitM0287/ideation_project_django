from django.db.models import query
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from logging_config.logger import get_logger
import pandas
from passenger_app.utils import store_data, convert_to_list
from passenger_app.models import passenger_movement
from django.conf import settings
from passenger_app.models import passenger_movement

# Logger configuration
logger = get_logger()

class PageNotFound(Exception):
    pass

class PassengerAPIView(APIView):
    """
        PassengerAPIView: Store Passenger data, Get passenger data 
    """
    def post(self, request):
        """
            This method is used to store passenger data from csv file.
            :param request: It's accept .csv file as parameter.
            :return: It's return response that data is successfully or not into database.
        """
        try:
            data = pandas.read_csv(request.data['file'])
            # Convert csv to dict
            data = data.to_dict('dict')
            # Truncate table
            passenger_movement.objects.all().delete()
            # Store data
            for index in range(len(data['Date'])):
                store_data(date= data['Date'][index], arrivals_actual_counts= data['ArrivalsActualCounts'][index], departures_actual_counts=data['DeparturesActualCounts'][index])
            # Data stored successfully into database
            return Response({'success': True, 'message': 'All data successfully stored into database.'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False, 'message': 'Oops! Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
            This method is used to get data from databse.
            :param request: It's accept page_no as parameter.
            :return: It's return response that getting data successfully from database.
        """
        try:
            # Calculate number of pages
            total = len(list(passenger_movement.objects.raw('SELECT id FROM passenger_app_passenger_movement')))
            num_pages = round(total/int(settings.PAGE_CONTENT))
            # Check given page no is exist or not
            if int(request.GET.get('page_no')) > num_pages:
                raise PageNotFound
            # Calculate OFFSET value
            offset_value = (int(request.GET.get('page_no'))-1) * settings.PAGE_CONTENT
            # Execute query
            for data in passenger_movement.objects.raw('SELECT * FROM passenger_app_passenger_movement LIMIT %s OFFSET %s ROWS', [settings.PAGE_CONTENT, offset_value]):
                list_data = convert_to_list(str(data.Date)[0:10], data.ArrivalsActualCounts, data.DeparturesActualCounts)
            # Getting data successfully from database
            return Response({'success': True, 'message': 'Getting all data successfully from database.', "num_of_pages": num_pages, "page_no": request.GET.get('page_no'), "data": list_data}, status=status.HTTP_200_OK)
        except PageNotFound as e:
            logger.exception(e)
            return Response({'success': False, "num_of_pages": num_pages, "page_no": request.GET.get('page_no'), 'message': 'Page not found!'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False, 'message': 'Oops! Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)
