from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,permissions
from.models import VitalSigns
from. serializers import VitalSignsSerializers

class VitalSignsViewSet(viewsets.ModelViewSet):
    queryset=VitalSigns.objects.all()
    serializer_class=VitalSignsSerializers
    permission_classes=[permissions.IsAuthenticated]