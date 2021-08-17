import datetime


def get_week_number(date: datetime.date) -> int:
    return (date.day - 1 + (date.weekday() - date.day + 1) % 7) // 7 + 1


def find_first_monday(year, month) -> datetime.date:
    date = datetime.date(year, month, 7)
    offset = -date.weekday()

    return date + datetime.timedelta(offset)


def get_last_day_of_month(year: int, month: int) -> datetime.date:
    return datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)


def get_month_weekdays(
        year: int,
        month: int,
        from_first_monday=False
) -> list[set[int]]:
    """
    Return a list of sets with every set a week with the day numbers
    in the given month of the given year.

    >>> get_month_weekdays(year=2021, month=8, from_first_monday=True)
    [
        {2, 3, 4, 5, 6, 7, 8},
        {9, 10, 11, 12, 13, 14, 15},
        {16, 17, 18, 19, 20, 21, 22},
        {23, 24, 25, 26, 27, 28, 29},
        {30, 31}
    ]
    """
    first_day = find_first_monday(year, month)
    if not from_first_monday:
        first_day = first_day.replace(day=1)

    last_day_of_month = get_last_day_of_month(year, month).day

    return [
        {
            day
            for day in range(start_day, start_day + 7)
            if day <= last_day_of_month
        }
        for start_day in range(first_day.day, last_day_of_month + 1, 7)
    ]
