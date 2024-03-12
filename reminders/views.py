from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reminder
from .serializers import ReminderSerializer

@api_view(['GET', 'POST'])
def create_reminder(request):
    if request.method == 'GET':
        reminders = Reminder.objects.all()
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
