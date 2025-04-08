from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Varos, Bejelentes
from .serializers import VarosSerializer, BejelentesSerializer

# Create your views here.

# Api visszaadja az osszes bejelentes adatat JSON formatumban
@api_view(['GET'])
def osszesBejelentes(request):
  osszes = Bejelentes.objects.all().order_by('-datum')
  serialized = BejelentesSerializer(osszes, many = True)
  return Response(serialized.data)

@api_view(['GET'])
def varosBejelentes(request, vnev):
  if request.method == 'GET':
    aktualisVaros = Varos.objects.get(varosNev = vnev)
    varosAdatok = Bejelentes.objects.filter(varos = aktualisVaros).order_by('-datum')
    serialized = BejelentesSerializer(varosAdatok, many=True)
    return Response(serialized.data)