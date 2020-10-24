from rest_framework import serializers

from activitytracker.models import ActivityTracker


class ActivityTrackerSerializer(serializers.ModelSerializer):

     username = serializers.SerializerMethodField('get_username')

     class Meta:
         model = ActivityTracker
         fields = '__all__'
    

     def get_username(self, activity_tracker):
         return activity_tracker.user.username


    