from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from stockmanagement.models import Category
from stockmanagement.models import SubCategory
from stockmanagement.models import Supplier
from stockmanagement.models import AddStockItem

from stockmanagement.api.serializers import CategorySerializer
from stockmanagement.api.serializers import SubCategorySerializer
from stockmanagement.api.serializers import SupplierSerializer
from stockmanagement.api.serializers import AddStockItemSerializer




#############   HANDLE ITEM CATEGORY REST HTTP RESQUESTS   #############

@api_view(['POST',])
@permission_classes([IsAuthenticated,])
def api_create_stock_items_category_view(request):
        if request.method == 'POST':
            serializer = CategorySerializer(Category(), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data='success', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def api_get_stock_items_category_view(request):
        try:
            category = Category.objects.all()
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CategorySerializer(category, many=True)
            return Response(serializer.data)


@api_view(['PUT',])
@permission_classes([IsAuthenticated,])
def api_update_stock_items_category_view(request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            data = {}
            serializer = CategorySerializer(category, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data['success'] = "Update success"
                return Response(data=data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
@permission_classes([IsAuthenticated,])
def api_delete_stock_item_category_view(request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            data = {}
            operation = category.delete()
            if operation:
                data['success'] = "Delete success"
            else:
                data['failure'] = "Delete failed"
            return Response(data=data)


#############   HANDLE ITEM SUB-CATEGORY REST HTTP RESQUESTS   #############

@api_view(['POST',])
@permission_classes([IsAuthenticated,])
def api_create_stock_item_subcategory_view(request, cat_pk):
        if request.method == 'POST':
            category = Category.objects.get(pk=cat_pk)
            subcat = SubCategory(categ=category)
            serializer = SubCategorySerializer(subcat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data='success', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def api_get_stock_item_subcategory_view(request):
        try:
              subcategory = SubCategory.objects.all()
        except SubCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = SubCategorySerializer(subcategory, many=True)
            return Response(serializer.data)


@api_view(['PUT',])
@permission_classes([IsAuthenticated,])
def api_update_stock_item_subcategory_view(request, pk):
        try:
            subcategory = SubCategory.objects.get(pk=pk)
        except SubCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            data = {}
            serializer = SubCategorySerializer(subcategory, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data['success'] = "Update success"
                return Response(data=data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
@permission_classes([IsAuthenticated,])
def api_delete_stock_item_subcategory_view(request, pk):
        try:
            subcategory = SubCategory.objects.get(pk=pk)
        except SubCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            data = {}
            operation = subcategory.delete()
            if operation:
                data['success'] = "Delete success"
            else:
                data['failure'] = "Delete failed"
            return Response(data=data)


#######################   GET SINGLE SUBCATEGORY ITEM   ##########################
@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def api_get_single_stock_item_subcategory_view(request, cat_pk):
        try:
              subcategory = SubCategory.objects.filter(categ=cat_pk)
        except SubCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = SubCategorySerializer(subcategory, many=True)
            return Response(serializer.data)  


#############   HANDLE SUPPLIER REST HTTP RESQUESTS   #############

@api_view(['POST',])
@permission_classes([IsAuthenticated,])
def api_create_stock_item_supplier_view(request):
        if request.method == 'POST':
            serializer = SupplierSerializer(Supplier(), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data='success', status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def api_get_stock_item_supplier_view(request):
        try:
            supplier = Supplier.objects.all()
        except Supplier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = SupplierSerializer(supplier, many=True)
            return Response(serializer.data)


@api_view(['PUT',])
@permission_classes([IsAuthenticated,])
def api_update_stock_item_supplier_view(request, pk):
        try:
            supplier = Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            data = {}
            serializer = SupplierSerializer(supplier, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data['success'] = "Update success"
                return Response(data=data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
@permission_classes([IsAuthenticated,])
def api_delete_stock_item_supplier_view(request, pk):
        try:
            supplier = Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            data = {}
            operation = supplier.delete()
            if operation:
                data['success'] = "Delete success"
            else:
                data['failure'] = "Delete failed"
            return Response(data=data)


#############   HANDLE STOCK ITEM REST HTTP RESQUESTS   #############

@api_view(['POST',])
@permission_classes([IsAuthenticated,])
def api_create_stock_item_view(request, cat_pk, subcat_pk, sup_pk):
        if request.method == 'POST':

            category = Category.objects.get(pk=cat_pk)
            subcategory = SubCategory.objects.get(pk=subcat_pk)
            supplier = Supplier.objects.get(pk=sup_pk)

            stock_item = AddStockItem(cat=category, subcat=subcategory, supplier=supplier)

            serializer = AddStockItemSerializer(stock_item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data='success', status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def api_get_stock_item_view(request):
        try:
            add_stock_item = AddStockItem.objects.distinct() 
        except AddStockItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = AddStockItemSerializer(add_stock_item, many=True)
            return Response(serializer.data)


@api_view(['PUT',])
@permission_classes([IsAuthenticated,])
def api_update_stock_item_view(request, pk):
        try:
            add_stock_item = AddStockItem.objects.get(pk=pk)
        except AddStockItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
             data = {}
             serializer = AddStockItemSerializer(add_stock_item, data=request.data, partial=True)

             if serializer.is_valid():
                serializer.save()
                data['success'] = "Update success"
                return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
@permission_classes([])
def api_delete_stock_item_view(request, pk):
        try:
            add_stock_item = AddStockItem.objects.get(pk=pk)
        except AddStockItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            data = {}
            operation = add_stock_item.delete()
            if operation:
                data['success'] = "Delete success"
            else:
                data['failure'] = "Delete failed"
            return Response(data=data)


########################   GET SINGLE STOCK ITEM    ################################

@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def api_get_single_stock_item_view(request, pk):
        try:
            add_stock_item = AddStockItem.objects.get(pk=pk)
        except AddStockItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = AddStockItemSerializer(add_stock_item, many=False)
            return Response(serializer.data)
