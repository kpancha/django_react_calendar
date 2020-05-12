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
        print('before')
        googleId = quickstart.addEvent(summary,location,description,startTime,endTime)
        #event_list = list(Event.objects.all())
        #if len(event_list) != 0:
            #print(event_list[len(event_list) - 1].summary)
            #print(event_list[len(event_list) - 1].googleId)
        validated_data['googleId'] = googleId
        #print(validated_data)
        return Event.objects.create(**validated_data)
    def delete(self, req, *args, **kwargs):
        print('hello')
        print(Event.objects.googleId)
        quickstart.deleteEvent(Event.objects.googleId)
        question = get_object_or_404(Question, pk=kwargs['id'])
        question.delete()
        return Response("Question deleted", status=status.HTTP_204_NO_CONTENT)
        #return Event.objects.destroy(**validated_data)
