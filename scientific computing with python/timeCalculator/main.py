def add_time(start, duration, startDayOfWeek = None):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Parsing logic for day of the week index
    startDayOfWeekIndex = 0
    if startDayOfWeek != None:
        for day in days_of_week:
            if day.lower() == startDayOfWeek.lower():
                startDayOfWeekIndex = days_of_week.index(day)
                break
    
    # Parsing logic for start time
    start_time_and_period = start.split(" ")
    start_hours = int(start_time_and_period[0].split(":")[0])
    start_minutes = int(start_time_and_period[0].split(":")[1])
    start_period = start_time_and_period[1]
    if start_period == "PM":
        start_hours += 12

    # Parsing logic for duration time
    duration_hours = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])
    if int(duration_minutes) > 60:
        duration_minutes = 60

    # Calculation logic
    sum_hours = start_hours + duration_hours
    sum_minutes = start_minutes + duration_minutes
    if sum_minutes >= 60:
        sum_hours += 1
    days_later = int(sum_hours / 24)


    new_hours = sum_hours - (days_later * 24)
    new_munites = sum_minutes
    if new_munites >= 60:
        new_munites = new_munites - 60

    new_hours_to_print = new_hours - 12 if new_hours > 12 else new_hours
    new_minutes_to_print = "00" if new_munites == 0 else str(new_munites)
    if len(new_minutes_to_print) == 1:
        new_minutes_to_print = "0" + new_minutes_to_print

    days_later_string = ("(" + str(days_later) + " days later)")
    if days_later == 1:
        days_later_string = "(next day)"
    if days_later == 0:
        days_later_string = ""

    # To get day of the week
    new_day_week_index = startDayOfWeekIndex + days_later
    while new_day_week_index >= 7:
        new_day_week_index -= 7
    new_day_week_to_print = "" 
    if startDayOfWeek != None:
        new_day_week_to_print = days_of_week[new_day_week_index] if new_day_week_index < 7 else days_of_week[new_day_week_index - 7]

    # Result
    new_period_to_print = (" PM" if new_hours > 12 or (new_hours == 12 and start_period == "AM")else " AM")
    new_time = ("12" if new_hours_to_print == 0 else str(new_hours_to_print)) + ":" + new_minutes_to_print + new_period_to_print + (", " + new_day_week_to_print if new_day_week_to_print != "" else "") + (" " + days_later_string if days_later_string != "" else "")
    return new_time

print(add_time('11:43 AM', '00:20'))