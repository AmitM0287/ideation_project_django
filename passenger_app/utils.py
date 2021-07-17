from passenger_app.models import passenger_movement
from datetime import datetime


def store_data(date, arrivals_actual_counts, departures_actual_counts):
    """
        This method is used to store passenger data into database.
        :param date: It's accept date as parameter.
        :param arrivals_actual_counts: It's accept arrivals_actual_counts as parameter.
        :param departures_actual_counts: It's accept departures_actual_counts as parameter.
        :return: None
    """
    try:
        # Convert given date to datetime
        date = convert_to_datetime(date)
        passenger = passenger_movement(Date= date, ArrivalsActualCounts= arrivals_actual_counts, DeparturesActualCounts=departures_actual_counts)
        # Save data into database
        passenger.save()
    except Exception as e:
        raise Exception


def convert_to_datetime(string):
    """
        This method is used to convert string to datetime.
        :param string: It's accept string as parameter.
        :return: It's return datetime.
    """
    try:
        # 1921M01 to 1921-01-00 00:00:00
        string = string.replace('M', '')
        date_time = datetime.strptime(string, '%Y%m')
        return date_time.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        raise Exception
