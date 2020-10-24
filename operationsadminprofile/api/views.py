from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from account.models import Account
from operationsadminprofile.models import OperationsAdminProfile
from operationsadminprofile.api.serializers import OperationsAdminProfileSerializer



@api_view(['POST',])
@permission_classes([IsAuthenticated,])
def api_create_operations_admin_profile_view(request):
        if request.method == 'POST':
            try:
                account = Account.objects.get(pk=request.user.pk)
                profile = OperationsAdminProfile(user=account)
            except OperationsAdminProfile.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            if request.method == 'POST':
                serializer = OperationsAdminProfileSerializer(profile, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def api_get_operations_admin_profile_view(request):
        try:
            profile = OperationsAdminProfile.objects.filter(user_id=request.user.pk)
        except OperationsAdminProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = OperationsAdminProfileSerializer(profile, many=True)
            return Response(serializer.data)


@api_view(['PUT',])
@permission_classes([IsAuthenticated,])
def api_update_operations_admin_profile_view(request, pk):
        try:
            profile = OperationsAdminProfile.objects.get(pk=pk)
        except OperationsAdminProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            data = {}
            serializer = OperationsAdminProfileSerializer(profile, data=request.data , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

