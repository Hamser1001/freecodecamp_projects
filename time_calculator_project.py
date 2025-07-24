def add_time(start, duration, day=""):
    # Days of the week

    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    # Take day string
    day = day.upper().capitalize()

    # Split start by space to separate time and period
    time_part, period = start.split()  # ['3:00', 'PM']
    # Split time part by colon to get hours and minutes
    hours, minutes = map(int, time_part.split(":"))

    # Split duration by space to separate time and period
    duration_hours, duration_minutes = map(int, duration.split(":"))  # ['3:00']

    # Invalid hour and minutes
    if hours > 12 or minutes > 60 or duration_minutes > 60:
        return "Error"

    # Initlize Days added counter
    days_counter = 0

    # New hour
    new_hour = hours + duration_hours
    new_minutes = minutes + duration_minutes

    # If new minute is more than 60
    if new_minutes >= 60:
        new_hour += 1
        new_minutes -= 60

    # if i reach 12 PM shoud add +1 day and change period to AM

    # This part should be in While loop
    while new_hour >= 12:
        if new_hour == 12:
            # Change AM to PM or the opposite
            if period == "AM":
                period = "PM"
            else:
                period = "AM"
                days_counter += 1
            break
        elif new_hour > 12:
            new_hour -= 12
            if period == "AM":
                period = "PM"
            else:
                period = "AM"
                days_counter += 1

        # Determine current day index
    if day in days:
        index = days.index(day)
        day = days[(index + days_counter) % len(days)]

    # Determine text day of result
    # Build result string
    if days_counter == 1:
        days_text = " (next day)"
    elif days_counter > 1:
        days_text = f" ({days_counter} days later)"
    else:
        days_text = ""

    # Add day of the week if provided
    if day == "":
        new_time = f"{new_hour}:{new_minutes:02d} {period}{days_text}"
    elif day:
        new_time = f"{new_hour}:{new_minutes:02d} {period}, {day}{days_text}"
    else:
        new_time = f"{new_hour}:{new_minutes:02d} {period} {days_text}"

    return new_time

