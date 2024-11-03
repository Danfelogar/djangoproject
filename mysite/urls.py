# remember this project file named mysite was created with the command: django-admin startproject mysite
# remember start the server with the command: python manage.py runserver (3000 if you want to specify the port)
"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from myapp.views import sayHello
# from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # the first argument it's a prefix that will be added to the URL in the api for call
    path('', include('myapp.urls')),
]
