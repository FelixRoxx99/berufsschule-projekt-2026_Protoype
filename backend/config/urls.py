from django.contrib import admin
from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response

# WICHTIG: API-Funktion importieren!
from core.views import aufgaben_list

@api_view(['GET'])
def hello(request):
    return Response({"msg": "Hallo Felix! Deine API läuft."})

@api_view(['GET'])
def home(request):
    return Response({"msg": "Startseite läuft!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('', home),
    path('api/aufgaben/', aufgaben_list),
]
