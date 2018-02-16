def leapYears(year1, year2):
    """Returns a list of leap years from year1 to year2, inclusive."""

    leap_years = []
    for year in range(year1, year2 + 1):
        if year % 400 == 0:
            leap_years.append(year)
        elif year % 100 == 0:
            pass
        elif year % 4 == 0:
            leap_years.append(year)
    return leap_years

def SundayFirstofMonth(year1, year2, initial_day_of_week):
    """Returns a count of Sundays in years year1-year2 that fell on first of month.

    Parameters
    ----------
    year1: first year
    year2: last year
    initial_day_of_week: encoding of the first day of the week of the first day
                         of the first year. Sunday is 0, Saturday is 7.

    Output
    ----------
    The number of times the first day of a month fell on Sunday from year1 to year2.

    """

    day_count = initial_day_of_week
    count = 0
    if initial_day_of_week == 0:
        count += 1
    leap_years = leapYears(year1, year2)
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
    for year in range(year1, year2 + 1):
        if year in leap_years:
            leap_years[2] = 1
        for month in range(1, 12 +1):
            day_count += months[month]
            if day_count % 7 == 1:
                count += 1
        leap_years[2] = 0
    return count

if __name__ == "__main__":
    print(SundayFirstofMonth(1901, 2000, 1))
