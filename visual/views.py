from django.shortcuts import render
from rest_framework import viewsets

from visual.models import Visaul
from visual.serializers import VisualSerializer

# Create your views here.
class VisualViewSet(viewsets.ModelViewSet):
    queryset = Visaul.objects.all()
    serializer_class = VisualSerializer