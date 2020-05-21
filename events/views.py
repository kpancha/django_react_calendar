from django.shortcuts import render
from .models import Event
from .serializers import EventSerializer
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from . import quickstart

# Create your views here.

# view for handling GET, POST requests
class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        

# view for handling GET, PUT, DELETE requests
class EventRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        
    def update(self, request, *args, **kwargs):
        data = request.data
        summary = data['summary']
        location = data['location']
        description = data['description']
        startTime = data['start']
        endTime = data['end']
        queryset = Event.objects.get(id=kwargs['pk'])
        serializer = EventSerializer(queryset, data=data)
        if serializer.is_valid():
            serializer.save()
        quickstart.updateEvent(queryset.googleId, summary, location,description,startTime,endTime)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response()

    def perform_destroy(self, instance):
        quickstart.deleteEvent(instance.googleId)
        instance.delete()

# view for handling DELETE requests
# currently not used
class EventDestroy(generics.DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response()

    def perform_destroy(self, instance):
        quickstart.deleteEvent(instance.googleId)
        instance.delete()
