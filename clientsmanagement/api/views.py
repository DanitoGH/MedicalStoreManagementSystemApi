from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from account.models import Account
from clientsmanagement.models import Client
from clientsmanagement.api.serializers import ClientSerializer



@api_view(['POST',])
@permission_classes([IsAuthenticated,])
def api_create_client_view(request):
        if request.method == 'POST':
            try:
                account = Account.objects.get(pk=request.user.pk)
                client = Client(user=account)
            except Account.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            if request.method == 'POST':
                serializer = ClientSerializer(client, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def api_get_clients_view(request):
        try:
            client = Client.objects.all()
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ClientSerializer(client, many=True)
            return Response(data=serializer.data)


###################  GET CLIENT BY ID  ###################

@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def api_get_single_client_view(request, c_id):
        try:
            client = Client.objects.get(pk=c_id)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ClientSerializer(client)
            return Response(data=serializer.data)


###################  FILTER CLIENT BY USER ID  ##################

@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def api_get_current_client_view(request):
        try:
            client = Client.objects.get(user=request.user.pk)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ClientSerializer(client)
            return Response(data=serializer.data)


@api_view(['PUT',])
@permission_classes([IsAuthenticated,])
def api_update_client_view(request, c_id):
        try:
            client = Client.objects.get(pk=c_id)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            data = {}
            serializer = ClientSerializer(client, data=request.data , partial=True)
            if serializer.is_valid():
                serializer.save()
                data['success'] = "Update success"
                data['response'] = serializer.data
                return Response(data=data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
@permission_classes([IsAuthenticated,])
def api_delete_client_view(request, pk):
        if request.user.is_admin and request.user.is_staff:
            try:
                client = Client.objects.get(pk=pk)
            except Client.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        user = request.user
        if user.is_admin and not user.is_staff:
            return Response({'response': "Sorry, you don't have permission to delete this client!"})

        if request.method == 'DELETE':
            data = {}
            operation = client.delete()
            if operation:
                data['success'] = "Delete success"
            else:
                data['failure'] = "Delete failed"
            return Response(data=data)


