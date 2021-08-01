from django.contrib import admin

from apps.education.models.activity import Activity
from apps.education.models.child import Child

admin.site.register(Child)
admin.site.register(Activity)
