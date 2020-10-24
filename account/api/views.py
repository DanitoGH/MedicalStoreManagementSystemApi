from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from account.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token



##########   ACCOUNT REGISTRATION   ##########
@api_view(['POST',])
@permission_classes([])
def registration_view(request, account_type):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            if account_type == 'operations':
                user = serializer.registerOperationsAdmin()
            elif account_type == 'client':
                user = serializer.resgisterClientAdmin()

            data['status'] = "success"
            data['user_id'] = user.pk
            data['email'] = user.email
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data['redirect_to'] = '/' if user.is_admin and user.is_staff else '/client-admin' 
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


###########   LOGIN WITH CUSTOM AUTH TOKEN   ########
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username,
            'redirect_to': '/' if user.is_admin and user.is_staff else '/client-admin' 
        })
        