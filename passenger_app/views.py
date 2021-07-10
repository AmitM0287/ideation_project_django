from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from logging_config.logger import get_logger
import pandas

# Logger configuration
logger = get_logger()

class PassengerAPIView(APIView):
    """
        PassengerAPIView: Store Passenger data, Get passenger data 
    """
    def post(self, request):
        """
            This method is used to store passenger data from xlsx file.
            :param request: It's accept .xlsx file as parameter.
            :return: It's return response that data is successfully or not into database.
        """
        try:
            data = pandas.read_excel(request.data['file'])
            # Convert xlsx to dict
            data = data.to_dict('dict')
            # Print data
            for index in range(len(data['Name'])):
                print(data['Name'][index], data['Branch'][index], data['Student Code'][index], data['Email'][index], data['Phone'][index], data['Grade'][index])
            # Data stored successfully into database
            return Response({'success': True, 'message': 'All data successfully stored into database.'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False, 'message': 'Oops! Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)
