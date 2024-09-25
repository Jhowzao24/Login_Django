from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer
from django.http import HttpResponse

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


def Indexing(request):
    return HttpResponse('<center><h1>Welcome to the django Back-End Environment</h1></center><hr/><br/><center><h3>Here will appear the datas of the uers from your project</h3><br/><br/><img src="https://maxmautner.com/public/images/django.gif" alt="django"/></center>')