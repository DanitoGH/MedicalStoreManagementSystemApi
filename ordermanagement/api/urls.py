from django.urls import path

from ordermanagement.api.views import (
       api_create_order_view,
       api_get_all_orders_view,
       api_get_client_orders_view,
       api_update_order_view,
       api_delete_order_view,
     )

app_name = "ordermanagement"

urlpatterns = [
      path('get-all-orders', api_get_all_orders_view, name="get_all_orders"),
      path('get-client-orders/<c_id>', api_get_client_orders_view, name="get_client_orders"),
      path('create-order', api_create_order_view, name="create_order"),
      path('update-order/<pk>', api_update_order_view, name="update_order"),
      path('delete-order/<pk>', api_delete_order_view, name="delete_order"),
]