from django.shortcuts import render
from .models import Event
from .serializers import EventSerializer
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from . import quickstart

# Create your views here.

# view for handling GET and POST requests
class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        

# view for handling GET and DELETE requests
class EventRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response()

    def perform_destroy(self, instance):
        #print('id: ' + str(instance.googleId))
        quickstart.deleteEvent(instance.googleId)
        instance.delete()
