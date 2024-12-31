
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home (request):
    return HttpResponse('Hello world this is django project and working properly.')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
