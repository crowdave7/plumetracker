import numpy as np
import datetime

def get_datetime_objects(time_params):
    """
    Generates an array of datetime objects at 15 minute intervals within the
    input time bounds
    :param time_params: an array of integers corresponding to time bounds
    :return datetimes: array of datetime objects
    """

    # Get the lower and upper bound of the datetime objects
    datetime_lower = datetime.datetime(time_params[0], time_params[2],
                                       time_params[4], time_params[6],
                                       time_params[8])
    datetime_upper = datetime.datetime(time_params[1], time_params[3],
                                       time_params[5], time_params[7],
                                       time_params[9])

    # Get the difference between the two dates in minutes using a timedelta
    # object
    td = datetime_upper-datetime_lower
    mins_difference = divmod(td.days*86400+td.seconds, 60)[0]

    # Get an array of minute values with 15 minute intervals
    minutes_range = np.arange(0, mins_difference+15, 15)

    # Get an array of datetime objects for each 15 minute interval
    datetimes = np.array([datetime_lower + datetime.timedelta(minutes=i) for
                          i in minutes_range])
    return datetimes

## Perhaps a dateperiod object