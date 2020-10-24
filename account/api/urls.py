from django.urls import path
from account.api.views import registration_view
from account.api.views import CustomAuthToken


app_name = "account"

urlpatterns = [
      path('login',  CustomAuthToken.as_view(), name="login"),
      path('register/<account_type>', registration_view, name="register"),
]