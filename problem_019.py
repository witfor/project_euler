def SundayFirstofMonth(year1, year2):
    """Returns a count of Sundays in years year1-year2 that fell on first of month.

    Parameters
    ----------
    year1: first year
    year2: last year

    Output
    ----------
    The number of times the first day of a month fell on Sunday from year1 to year2.
    """

    # Dictionary of days in month modulo 7, which explains how many days forward
    # weekday changes in a month. For example, if January 1 is a Monday,
    # February 1 (+3) is a Wednesday.
    months = {
            1: 3,
            2: 0,
            3: 3,
            4: 2,
            5: 3,
            6: 2,
            7: 3,
            8: 3,
            9: 2,
            10: 3,
            11: 2,
            12: 3
            }
    day_count = findStartDay(1901)
    count = 0
    for year in range(year1, year2 + 1):
        if isLeapYear(year):
            months[2] = 1
        for month in range(1, 12 + 1):
            if day_count % 7 == 1:
                count += 1
            day_count += months[month]
        months[2] = 0
    return count

def findStartDay(year):
    """Returns the day of week year started on: Sunday is 1, Saturday is 7."""

    months = {
            1: 3,
            2: 0,
            3: 3,
            4: 2,
            5: 3,
            6: 2,
            7: 3,
            8: 3,
            9: 2,
            10: 3,
            11: 2,
            12: 3
            }
    # January 1, 1900 is a Monday.
    day_count = 1
    for year in range(1900, year + 1):
        if isLeapYear(year):
            months[2] = 1
        for month in range(1, 12 + 1):
            day_count += months[month]
        months[2] = 0
    return day_count % 7

def isLeapYear(year):
    """Returns True if year is a leap year."""

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(SundayFirstofMonth(1901, 2000))
