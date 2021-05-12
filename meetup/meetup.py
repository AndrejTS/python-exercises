from calendar import Calendar


days = {'Mo': 1, 'Tu': 2, 'We': 3, 'Th': 4, 'Fr': 5, 'Sa': 6, 'Su': 7} 


class MeetupDayException(Exception):
    pass


def meetup(year, month, week, day_of_week):
    day_of_week = days[day_of_week[0:2]]
    cal = Calendar().itermonthdates(year, month)
    lst = [] # possible days
    for day in cal:
        if day.isoweekday() == day_of_week:
            if day.month == month:
                lst.append(day)
    
    if week[0] in '12345':
        if len(lst) < int(week[0]):
            raise MeetupDayException('Day not found!')
        return lst[int(week[0]) - 1]
    elif week == 'last':
        return lst[-1]
    elif week == 'teenth':
        for x in lst:
            if x.day in range(13, 20):
                return x
