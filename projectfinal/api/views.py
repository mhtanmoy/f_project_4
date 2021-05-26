from django.shortcuts import render
from rest_framework import generics ,  permissions
from project.models import *
from .serializers import *

class CustomerUserList(generics.ListCreateAPIView):
    queryset=courses.objects.all()
    serializer_class=CoursesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save()


class CustomerUserUpdateList(generics.UpdateAPIView):
    queryset=courses.objects.all()
    serializer_class=CoursesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field='pk'
    def perform_create(self, serializer):
        serializer.save()

class ContactUserList(generics.ListCreateAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save()


class CustomerUserUpdateList(generics.UpdateAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field='pk'
    def perform_create(self, serializer):
        serializer.save()
