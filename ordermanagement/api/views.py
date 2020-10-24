from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from clientsmanagement.models import Client
from ordermanagement.models import CreateOrder
from stockmanagement.models import AddStockItem
from ordermanagement.api.serializers import CreateOrderSerializer




@api_view(['POST',])
@permission_classes([IsAuthenticated,])
def api_create_order_view(request):
        if request.method == 'POST':
            if request.user.is_admin and request.user.is_staff:
                return Response({"You'ur not authorized to create an order!"})
                
            try:
                client = Client.objects.get(pk=request.data['client'])
                item = AddStockItem.objects.get(pk=request.data['item'])
                create_order = CreateOrder(client=client, item=item)
            except Client.DoesNotExist or AddStockItem.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            if request.method == 'POST':
                data = {}
                serializer = CreateOrderSerializer(create_order, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    data['success'] = "Success"
                    return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def api_get_all_orders_view(request):
        try:
            orders = CreateOrder.objects.all()
        except CreateOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CreateOrderSerializer(orders, many=True)
            return Response(serializer.data)


##################    GET SINGLE CLIENT ORDERS    ##################
@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def api_get_client_orders_view(request, c_id):
        try:
            create_order = CreateOrder.objects.all()
            order = create_order.filter(client=c_id)
        except CreateOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CreateOrderSerializer(order, many=True)
            return Response(serializer.data)


@api_view(['PUT',])
@permission_classes([IsAuthenticated,])
def api_update_order_view(request, pk):
        try:
            create_order = CreateOrder.objects.get(pk=pk)
        except CreateOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            data = {}
            serializer = CreateOrderSerializer(create_order, data=request.data , partial=True)
            if serializer.is_valid():
                serializer.save()
                data['success'] = "Update success"
                return Response(data=data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
@permission_classes([IsAuthenticated,])
def api_delete_order_view(request, pk):
        if request.user.is_admin and request.user.is_staff:
            return Response({'response': "Sorry, you don't have permission to delete this order!"})

        try:
            create_order = CreateOrder.objects.get(pk=pk)
        except CreateOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            data = {}
            operation = create_order.delete()
            if operation:
                data['success'] = "Delete success"
            else:
                data['failure'] = "Delete failed"
            return Response(data=data)
