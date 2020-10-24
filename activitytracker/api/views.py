from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from account.models import Account
from activitytracker.models import ActivityTracker
from activitytracker.api.serializers import ActivityTrackerSerializer



@api_view(['POST',])
@permission_classes([IsAuthenticated,])
def api_create_user_activity_view(request):
        if request.method == 'POST':
                try:
                    user = Account.objects.get(pk=request.user.id)
                    add_new_activity = ActivityTracker(user=user)
                except ActivityTracker.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                if request.method == 'POST':
                    serializer = ActivityTrackerSerializer(add_new_activity, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def api_get_user_activities_view(request):
        try:
            if request.user.is_admin and request.user.is_staff:
                user_activities = ActivityTracker.objects.all()
            elif request.user.is_admin and not request.user.is_staff:
                activity_tracker = ActivityTracker.objects.all()
                user_activities = activity_tracker.filter(user=request.user.id)
        except ActivityTracker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ActivityTrackerSerializer(user_activities, many=True)
            return Response(serializer.data)
           
