from django.urls import path

from stockmanagement.api.views import (
       api_create_stock_items_category_view,
       api_get_stock_items_category_view,
       api_update_stock_items_category_view,
       api_delete_stock_item_category_view,
     )

from stockmanagement.api.views import (
       api_create_stock_item_subcategory_view,
       api_get_stock_item_subcategory_view,
       api_get_single_stock_item_subcategory_view,
       api_update_stock_item_subcategory_view,
       api_delete_stock_item_subcategory_view,
     )

from stockmanagement.api.views import (
       api_get_stock_item_supplier_view,
       api_create_stock_item_supplier_view,
       api_update_stock_item_supplier_view,
       api_delete_stock_item_supplier_view,
     )

from stockmanagement.api.views import (
       api_create_stock_item_view,
       api_get_stock_item_view,
       api_get_single_stock_item_view,
       api_update_stock_item_view,
       api_delete_stock_item_view,
     )

app_name = "stockmanagement"


urlpatterns = [
      #########  CATEGORY VIEWS URLS   ############
      path('get-category', api_get_stock_items_category_view, name="get_category"),
      path('create-category', api_create_stock_items_category_view, name="create_category"),
      path('update-category/<pk>', api_update_stock_items_category_view, name="update_category"),
      path('delete-category/<pk>', api_delete_stock_item_category_view, name="delete_category"),

      #########  SUB-CATEGORY VIEWS URLS   ############
      path('get-subcategory', api_get_stock_item_subcategory_view, name="get_subcategory"),
      path('get-single-subcategory/<cat_pk>', api_get_single_stock_item_subcategory_view, name="get_single_subcategory"),
      path('create-subcategory/<cat_pk>', api_create_stock_item_subcategory_view, name="create_subcategory"),
      path('update-subcategory/<pk>', api_update_stock_item_subcategory_view, name="update_subcategory"),
      path('delete-subcategory/<pk>', api_delete_stock_item_subcategory_view, name="delete_subcategory"),

      #################  SUPPLIER VIEWS URLS   ###################
      path('create-supplier', api_create_stock_item_supplier_view, name="create_supplier"),
      path('get-supplier', api_get_stock_item_supplier_view, name="get_supplier"),
      path('update-supplier/<pk>', api_update_stock_item_supplier_view, name="update_supplier"),
      path('delete-supplier/<pk>', api_delete_stock_item_supplier_view, name="delete_supplier"),

      ################  STOCK ITEM VIEWS URLS   ################
      path('create-stock-item/<cat_pk>/<subcat_pk>/<sup_pk>', api_create_stock_item_view, name="create_stock_item"),
      path('get-stock-item', api_get_stock_item_view, name="get_stock_item"),
      path('get-single-stock-item/<pk>', api_get_single_stock_item_view, name="get_single_stock_item"),
      path('update-stock-item/<pk>', api_update_stock_item_view, name="update_stock_item"),
      path('delete-stock-item/<pk>', api_delete_stock_item_view, name="delete_stock_item"),
]