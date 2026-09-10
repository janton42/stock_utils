from datetime import date

def days_between(start, end):
    d0 = date(start.year, start.month, start.day)
    d1 = date(end.year, end.month, end.day)
    delta = d1 - d0
    return delta.days


class DateObject:
    
    def __init__(self, **kwargs):
        self.year = kwargs['year']
        self.month = kwargs['month']
        self.day = kwargs['day']


if __name__ == '__main__':
    start_in = input('Enter a start date as comma-separated integers (YYYY, MM, DD): ')
    end_in = input('Enter an end date as comma-separated integers (YYYY, MM, DD): ')
    start_ints = start_in.split(',')
    end_ints =end_in.split(',')
    start = DateObject(year = int(start_ints[0]), month = int(start_ints[1]), day = int(start_ints[2]))
    end = DateObject(year = int(end_ints[0]), month = int(end_ints[1]), day = int(end_ints[2]))
    diff = days_between(start, end)
    print(f'There are {diff} days between {start.year}, {start.month}, {start.day} and {end.year}, {end.month}, {end.day}')


