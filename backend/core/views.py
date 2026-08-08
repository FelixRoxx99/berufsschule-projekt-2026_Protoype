from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Aufgabe

@api_view(['GET'])
def aufgaben_list(request):
    daten = [
        {
            "id": a.id,
            "titel": a.titel,
            "beschreibung": a.beschreibung
        }
        for a in Aufgabe.objects.all()
    ]
    return Response(daten)


