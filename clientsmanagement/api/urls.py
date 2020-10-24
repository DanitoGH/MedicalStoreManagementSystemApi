from django.urls import path

from clientsmanagement.api.views import (
       api_create_client_view,
       api_get_clients_view,
       api_get_single_client_view,
       api_get_current_client_view,
       api_update_client_view,
       api_delete_client_view,
     )

app_name = "clientsmanagement"

urlpatterns = [
      path('get-clients', api_get_clients_view, name="get_clients"),
      path('get-current-client', api_get_current_client_view, name="get_current_client"),
      path('get-single-client/<c_id>', api_get_single_client_view, name="get_single_client"),
      path('create-client', api_create_client_view, name="create_client"),
      path('update-client/<c_id>', api_update_client_view, name="update_client"),
      path('delete-client', api_delete_client_view, name="delete_client"),
]