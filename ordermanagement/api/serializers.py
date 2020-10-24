from rest_framework import serializers

from ordermanagement.models import CreateOrder



class CreateOrderSerializer(serializers.ModelSerializer):

    hospital_name = serializers.SerializerMethodField('get_hospital_name')
    item_id = serializers.SerializerMethodField('get_ordered_item_id')
    item = serializers.SerializerMethodField('get_ordered_item')
    stock_qty = serializers.SerializerMethodField('get_ordered_item_stock_qty')
    category = serializers.SerializerMethodField('get_item_category')
    subcategory = serializers.SerializerMethodField('get_item_subcategory')
    unit = serializers.SerializerMethodField('get_item_unit')

    class Meta:
        model = CreateOrder
        fields = '__all__'
        
    def get_hospital_name(self, create_order):
        return create_order.client.hospital_name

    def get_ordered_item_id(self, create_order):
        return create_order.item.id    

    def get_ordered_item(self, create_order):
        return create_order.item.name
    
    def get_ordered_item_stock_qty(self, create_order):
        return create_order.item.quantity

    def get_item_category(self, create_order):
        return create_order.item.cat.name
    
    def get_item_subcategory(self, create_order):
        return create_order.item.subcat.name
    
    def get_item_unit(self, create_order):
        return create_order.item.unit