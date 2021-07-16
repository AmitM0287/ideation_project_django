from passenger_app.models import passenger_movement


def store_data(date, arrivals_actual_counts, departures_actual_counts):
    """
        This method is used to store passenger data into database.
        :param date: It's accept date as parameter.
        :param arrivals_actual_counts: It's accept arrivals_actual_counts as parameter.
        :param departures_actual_counts: It's accept departures_actual_counts as parameter.
        :return: None
    """
    try:
        passenger = passenger_movement(Date= date, ArrivalsActualCounts= arrivals_actual_counts, DeparturesActualCounts=departures_actual_counts)
        # Save data into database
        passenger.save()
    except Exception as e:
        raise Exception
