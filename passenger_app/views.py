from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from logging_config.logger import get_logger
import pandas
from passenger_app.utils import store_data
from passenger_app.models import passenger_movement
from django.core.paginator import Paginator, EmptyPage

# Logger configuration
logger = get_logger()

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
            # passenger_movement.truncate()
            # Print data
            for index in range(len(data['Date'])):
                duplicate = store_data(date= data['Date'][index], arrivals_actual_counts= data['ArrivalsActualCounts'][index], departures_actual_counts=data['DeparturesActualCounts'][index])
            if duplicate > 0:
                # Duplicate records found
                return Response({'success': True, 'message': 'Database updated successfully.', 'warnings': str(duplicate) + ' duplicate records found!'}, status=status.HTTP_200_OK)
            else:
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
            passenger_data = passenger_movement.objects.all()
            paginator = Paginator(list(passenger_data.values()), 20)
            data = paginator.page(request.data.get('page_no'))
            # Getting data successfully from database
            return Response({'success': True, 'message': 'Getting all data successfully from database.', "num_of_pages": paginator.num_pages, "page_no": request.data.get('page_no'), "data": data.object_list}, status=status.HTTP_200_OK)
        except EmptyPage as e:
            logger.exception(e)
            return Response({'success': False, "num_of_pages": '1 to ' + str(paginator.num_pages), "page_no": request.data.get('page_no'), 'message': 'Page not found!'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False, 'message': 'Oops! Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)
