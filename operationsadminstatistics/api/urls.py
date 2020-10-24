from django.urls import path

from operationsadminstatistics.api.views import api_get_order_statistics_view

app_name = "operationsadminstatistics"

urlpatterns = [
      path('get-order-stats', api_get_order_statistics_view, name="get_order_stats"),
]