# Write function that counts number of days between two dates
# Write function that returns new date that is x days away from
# the given date, when x is positive it returns future date,
# if x is negative returns past date
from datetime import date, timedelta


def count_days(date_one: date, date_two: date):
    delta = date_one - date_two
    return abs(delta.days)


def date_from(start_date: date, days_difference: int):
    delta = timedelta(days=days_difference)
    return start_date + delta
