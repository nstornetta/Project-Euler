'''Want to find number of Sundays between 1 Jan 1901 and 31 Dec 2000 that
fell on the first of the month. '''

from datetime import date, timedelta

def count_sundays(start_year,start_month,start_day,end_date):
    current_date = date(start_year,start_month,start_day)
    sunday_counter = 0

    while current_date != date(2000,12,31) + timedelta(days=1):
        if date.weekday(current_date) == 6 and calendar_date=='01':
            sunday_counter += 1
        current_date += timedelta(days=1)
        calendar_date = str(current_date)
        calendar_date = calendar_date[-2:]
    return sunday_counter
