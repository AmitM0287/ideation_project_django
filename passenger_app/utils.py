from django.db.models.aggregates import Count
from passenger_app.models import passenger_movement


# Declare count as global variable
global count
# Set count value to 0
count = 0

def store_data(date, arrivals_actual_counts, departures_actual_counts):
    """
        This method is used to store passenger data into database.
        :param date: It's accept date as parameter.
        :param arrivals_actual_counts: It's accept arrivals_actual_counts as parameter.
        :param departures_actual_counts: It's accept departures_actual_counts as parameter.
        :return: It's return response that how many duplicate records found.
    """
    try:
        # Check if there is any duplicate entries or not
        if passenger_movement.objects.filter(Date=date).exists():
            globals()['count'] += 1
        else:
            passenger = passenger_movement(Date= date, ArrivalsActualCounts= arrivals_actual_counts, DeparturesActualCounts=departures_actual_counts)
            # Save data into database
            passenger.save()
        # Return how many duplicate records found
        return globals()['count']
    except Exception as e:
        raise Exception
