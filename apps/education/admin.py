from django.contrib import admin

from apps.education.models.activity import Activity
from apps.education.models.child import Child
from apps.education.models.subject import Subject
from apps.education.models.meal_menu import MealMenu

admin.site.register(Child)
admin.site.register(Activity)
admin.site.register(Subject)
admin.site.register(MealMenu)
