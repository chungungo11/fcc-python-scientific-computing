def add_time(start, duration, *start_day):
    # Split and assign start input
    start_hour = start.split(":")[0]
    start_minutes = start.split(":")[1].split(" ")[0]
    start_period = start.split(":")[1].split(" ")[1]

    # Split and assign duration input
    duration_hour = duration.split(":")[0]
    duration_minutes = duration.split(":")[1]

    # Calculate total amount of hours
    total_hours = int(start_hour) + int(duration_hour)
    # Add 12 hours if period is second half of day
    if start_period == 'PM':
        total_hours += 12

    # Calculate total amount of minutes and remaining minutes
    total_minutes = int(start_minutes) + int(duration_minutes)
    # Add one hour if total minutes exceeds 60
    if total_minutes > 60:
        remaining_minutes = total_minutes % 60
        total_hours += 1
    else:
        remaining_minutes = total_minutes

    # Calculate total amount of days and remaining hours
    total_days = 0
    while total_hours >= 24:
        total_hours -= 24
        total_days += 1
    remaining_hours = total_hours % 24

    # Determine and assign future hour & correct period
    if remaining_hours < 1:
        future_hour = 12
        future_period = 'AM'
    elif remaining_hours >= 1 and remaining_hours < 12:
        future_hour = remaining_hours
        future_period = 'AM'
    elif remaining_hours >= 12 and remaining_hours < 13:
        future_hour = remaining_hours
        future_period = 'PM'
    else:
        future_hour = remaining_hours - 12
        future_period = 'PM'

    # Determine and assign future minutes
    if remaining_minutes < 10:
        future_minutes = '0' + str(remaining_minutes)
    else:
        future_minutes = remaining_minutes

    # Create list of all days in week
    days_of_week = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]

    # Convert user input (start_day) into string
    def convertTuple(tup):
        string = ''
        for item in tup:
            string = string + item
        return string.lower().capitalize()

    # Determine future day when user inputs starting day
    if start_day:
        start_day = convertTuple(start_day)
        start_day_index = days_of_week.index(start_day)
        future_day_index = start_day_index + total_days
        # Prevent index being out of reach
        while future_day_index > (len(days_of_week) - 1):
            future_day_index -= len(days_of_week)
        future_day = days_of_week[future_day_index]

    # Default future time (string)
    future_time = f'{future_hour}:{future_minutes} {future_period}'

    # Future time (string) if user did not enter a starting day
    if not start_day:
        if total_days == 0:
            future_time
        elif total_days == 1:
            future_time = future_time + f' (next day)'
        else:
            future_time = future_time + f' ({total_days} days later)'

    # Future time (string) if user entered a starting day
    if start_day:
        if total_days == 0:
            future_time = future_time + f', {future_day}'
        elif total_days == 1:
            future_time = future_time + f', {future_day} (next day)'
        else:
            future_time = future_time + f', {future_day} ({total_days} days later)'

    print(future_time)
    return future_time


add_time('8:16 PM', '466:02', 'tuesday')