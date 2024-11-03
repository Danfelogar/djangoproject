from django.db import models
# remember make migrations and migrate do with the following commands:
# python manage.py makemigrations for creating migrations
# python manage.py migrate for applying migrations
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    #this method allow me extend a model and return a string representation of the object
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # this foreignKey assign a project to a task and if the project is deleted the task is deleted as well
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    #this method allow me extend a model and return a string representation of the object
    def __str__(self):
        return self.title + '  -  ' + self.project.name