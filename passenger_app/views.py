from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from logging_config.logger import get_logger
import pandas
from passenger_app.utils import store_data

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
            # Print data
            for index in range(len(data['Date'])):
                duplicate = store_data(date= data['Date'][index], arrivals_actual_counts= data['ArrivalsActualCounts'][index], departures_actual_counts=data['DeparturesActualCounts'][index])
            if duplicate > 0:
                # Duplicate records found
                return Response({'success': True, 'message': 'Database updated successfully.', 'warnings': str(duplicate) + ' duplicate values found!'}, status=status.HTTP_200_OK)
            else:
                # Data stored successfully into database
                return Response({'success': True, 'message': 'All data successfully stored into database.'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False, 'message': 'Oops! Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)
