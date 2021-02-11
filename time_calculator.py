def add_time(start, duration, day='None'):
    s_index = start.index(":")
    d_index = duration.index(":")
    hours_to_add = int(duration[:d_index])
    minutes_to_add = int(duration[(d_index + 1):])
    days_to_add = 0

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    start_hours = int(start[:s_index])
    start_minutes = int(start[s_index + 1: start.index(' ')])
    am_pm = start[start.index(' ') + 1:]

    while hours_to_add > 24 * 7:
        days_to_add += 7
        hours_to_add -= 24 * 7
    while hours_to_add > 24:
        days_to_add += 1
        hours_to_add -= 24

    if minutes_to_add + start_minutes > 59:
        hours_to_add += 1
        final_minutes = minutes_to_add + start_minutes - 60
    else:
        final_minutes = minutes_to_add + start_minutes

    if hours_to_add + start_hours > 23:
        days_to_add += 1
        final_hours = hours_to_add + start_hours - 24
    else:
        final_hours = hours_to_add + start_hours


    if final_hours > 11:
        if final_hours > 12:
            final_hours -= 12

        if am_pm == "AM":
            am_pm = "PM"
        else:
            am_pm = "AM"
            days_to_add += 1


    if final_hours == 0:
        final_hours = "12"
        if am_pm == "AM":
            am_pm = "PM"
        else:
            am_pm = "AM"
            days_to_add += 1

    if final_minutes < 10:
        final_minutes = "0" + str(final_minutes)

    final_time = str(final_hours) + ":" + str(final_minutes) + " " + am_pm

    if day != 'None':
        day = day.lower()
        index = 0
        days_passed = days_to_add
        for element in days:
            if element.lower() == day:
                index = days.index(element)
                break
        while days_passed > 7:
            days_passed -= 7

        if days_passed > len(days) - 1 - index:
            days_passed -= len(days) - 1 - index
            final_day = days[days_passed - 1].capitalize()
        else:
            index += days_passed
            final_day = days[index]

        final_time += ', ' + final_day

    if days_to_add == 1:
        days_later = ' (next day)'
        final_time += days_later
    elif days_to_add > 1:
        days_later = ' (' + str(days_to_add) + " days later)"
        final_time += days_later


    return final_time