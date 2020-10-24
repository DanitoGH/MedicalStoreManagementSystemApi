from django.urls import path

from operationsadminprofile.api.views import (
       api_create_operations_admin_profile_view,
       api_get_operations_admin_profile_view,
       api_update_operations_admin_profile_view,
     )

app_name = "operationsadminprofile"

urlpatterns = [
      path('get-profile', api_get_operations_admin_profile_view , name="get_profile"),
      path('create-profile', api_create_operations_admin_profile_view , name="create_profile"),
      path('update-profile/<pk>', api_update_operations_admin_profile_view , name="update_profile"),
]