from rest_framework import serializers

from stockmanagement.models import Category
from stockmanagement.models import SubCategory
from stockmanagement.models import Supplier
from stockmanagement.models import AddStockItem



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):

    cat_id = serializers.SerializerMethodField('get_category_id')
    cat_name = serializers.SerializerMethodField('get_category')
    
    class Meta:
        model = SubCategory
        fields = '__all__'
    
    def get_category_id(self, sub_category):
        return sub_category.categ.id

    def get_category(self, sub_category):
        return sub_category.categ.name


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class AddStockItemSerializer(serializers.ModelSerializer):

    cat_id = serializers.SerializerMethodField('get_category_id')
    cat = serializers.SerializerMethodField('get_category')
    subcat_id = serializers.SerializerMethodField('get_subcategory_id')
    subcat = serializers.SerializerMethodField('get_subcategory')
    reorder = serializers.SerializerMethodField('get_reorder_alert_quantity')
    supplier_id = serializers.SerializerMethodField('get_item_supplier_id')
    supplier = serializers.SerializerMethodField('get_item_supplier')


    class Meta:
        model = AddStockItem
        fields = '__all__'

    def get_category_id(self, add_stock_item):
        return add_stock_item.cat.id

    def get_category(self, add_stock_item):
        return add_stock_item.cat.name

    def get_subcategory_id(self, add_stock_item):
        return add_stock_item.subcat.id
    
    def get_subcategory(self, add_stock_item):
        return add_stock_item.subcat.name
    
    def get_reorder_alert_quantity(self, add_stock_item):
        return add_stock_item.cat.quantity
    
    def get_item_supplier_id(self, add_stock_item):
        return add_stock_item.supplier.id
    
    def get_item_supplier(self, add_stock_item):
        return add_stock_item.supplier.name
