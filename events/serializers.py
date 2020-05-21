from rest_framework import serializers
from .models import Event
from . import quickstart

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'summary', 'location', 'description', 'start', 'end')
        
    def create(self, validated_data):
        summary = validated_data['summary']
        location = validated_data['location']
        description = validated_data['description']
        startTime = validated_data['start']
        endTime = validated_data['end']
        googleId = quickstart.addEvent(summary,location,description,startTime,endTime)
        validated_data['googleId'] = googleId
        return Event.objects.create(**validated_data)
