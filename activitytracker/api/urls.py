from django.urls import path

from activitytracker.api.views import (
       api_get_user_activities_view,
       api_create_user_activity_view,
     )

app_name = "activitytracker"

urlpatterns = [
      path('get-user-activities', api_get_user_activities_view, name="get_user_activities"),
      path('add-activity', api_create_user_activity_view, name="add_activity"),
]