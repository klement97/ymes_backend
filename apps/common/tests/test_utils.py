import calendar
import datetime

from apps.common.utils import get_week_number


def test_get_week_number():
    for year in range(datetime.date.min.year, datetime.date.max.year + 1):
        for month in range(1, 12 + 1):
            month_days = calendar.monthcalendar(year, month)

            for week_number in range(1, len(month_days) + 1):
                for weekday in range(7):
                    day = month_days[week_number - 1][weekday]
                    if day == 0:
                        continue
                    date = datetime.date(year, month, day)

                    assert week_number == get_week_number(date), \
                        f'{date} week from calendar: {week_number},' \
                        f' from function: {get_week_number(date)}'
