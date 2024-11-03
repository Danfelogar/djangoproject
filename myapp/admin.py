from django.contrib import admin

from .models import Task, Project

# Register your models here.

#with this line we are registering the Project model to be shown in the admin interface
admin.site.register(Project)
admin.site.register(Task)