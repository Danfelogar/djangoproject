# remember this myapp file was created with the command: python manage.py startapp myapp
# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# import the models for querying the database
from .models import Task,Project
# import the get_object_or_404 function to get a single object from the database
from django.shortcuts import get_object_or_404, render, redirect
# import the form class for creating a new forms what will use in create_task
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request:str):
  title = "Welcome to the Django App!!!"
  return render(request, "index.html", {
    'title': title
  })

def sayHello(request:str, username:str):
  return HttpResponse("<h2>Hello, %s!</h2>" % username)

def about(request:str):
  username = "Danfelogar"
  return render(request, "about.html",{
    'username': username
  })

def projects(request:str):
  #  this line will query the database for all the projects and return them as a list of dictionaries for showing them as JSON
  projects = list(Project.objects.values())
  # its necessary to set safe=False to allow the serialization of the data
  # return JsonResponse(projects, safe=False)
  return render(request, "projects/projects.html",{
    'projects': projects
  })

def project(request:str, project_id:str):
  # project = Project.objects.get(id=project_id)
  project = get_object_or_404(Project, name=project_id)

  return HttpResponse("project: %s" % project.name)


def tasks(request:str):
  tasks = Task.objects.all()
  return render(request, "tasks/tasks.html", { 'tasks': tasks })

def create_task(request:str):
  if request.method == 'GET':
    return render(request, "tasks/create_task.html", {
      # ejecute the form class to create a new form
      'form': CreateNewTask()
    })
  else:
    Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=1)
    return redirect('tasks')

def create_project(request):
  if request.method == 'GET':
    return render(request, "projects/create_project.html", {
      'form': CreateNewProject()
    })
  else:
    Project.objects.create(name=request.POST['name'])
    return redirect('projects')

def project_detail(request:str, id: int):
  # project = Project.objects.get(id=id)
  project = get_object_or_404(Project, id=id)
  task = Task.objects.filter(project_id=id)
  return render(request, "projects/detail.html",{
    'project': project,
    'tasks': task
  })