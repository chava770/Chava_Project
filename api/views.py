from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from workers.models import Workers
from .serializers import WorkersSerializer


class GlobalPermission(IsAuthenticated):
    message = 'You must be authenticated to perform this action.'

class WorkersList(viewsets.ModelViewSet):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer
    permission_classes = [GlobalPermission]


