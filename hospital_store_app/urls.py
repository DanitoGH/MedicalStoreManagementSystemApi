from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),

    #REST FRAMEWORK URLS
    path('api/account/', include('account.api.urls', 'account_api')),
    path('auth/', obtain_auth_token),

    path('api/categories/', include('stockmanagement.api.urls', 'stockmanagement_category_api')),
    path('api/sub-categories/', include('stockmanagement.api.urls', 'stockmanagement_sub_category_api')),
    path('api/suppliers/', include('stockmanagement.api.urls', 'stockmanagement_supplier_api')),
    path('api/stock-item/', include('stockmanagement.api.urls', 'stockmanagement_stockt_item_api')),
    # path('api/category-management/', include('stockmanagement.api.urls', 'stockmanagement_category_management_api')),

    #ORDER MANAGEMENT URL
    path('api/orders/', include('ordermanagement.api.urls', 'ordermanagement_create_api')),

    #CLIENTS MANAGEMENT URL
    path('api/clients/', include('clientsmanagement.api.urls', 'clientsmanagement_clients_api')),

    #ACTIVITY TRACKER URL
    path('api/tracker/', include('activitytracker.api.urls', 'activitytracker_api')),

    #OPERATIONS ORDER STATISTICS URL
    path('api/operations-order-stats/', include('operationsadminstatistics.api.urls', 'operationsadminstatistics_api')),

    #CLIENTS ORDER STATISTICS URL
    path('api/clients-order-stats/', include('clientadminstatistics.api.urls', 'clientadminstatistics_api')),

    #OPERATIONS ADMIN PROFILE PAGE URL
    path('api/operations-admin-profile/', include('operationsadminprofile.api.urls', 'operations_admin_profile_api')),
]


