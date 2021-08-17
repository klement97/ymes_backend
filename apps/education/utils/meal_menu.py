import datetime

from django.utils import timezone

from apps.common.choices import Day
from apps.education.models import MealMenu


class MealMenuUtil:

    def get_meal_of_the_day(self, day: Day = None):
        day = day or timezone.now().weekday()
        meals = MealMenu.objects.filter(

        )
