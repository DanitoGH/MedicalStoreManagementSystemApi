from django.urls import path

from clientadminstatistics.api.views import api_get_client_statistics_view

app_name = "clientadminstatistics"

urlpatterns = [
      path('get-client-stats/<c_id>', api_get_client_statistics_view, name="get_client_stats"),
]