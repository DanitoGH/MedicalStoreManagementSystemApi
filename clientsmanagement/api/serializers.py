from rest_framework import serializers

from clientsmanagement.models import Client


class ClientSerializer(serializers.ModelSerializer):

    email = serializers.SerializerMethodField('get_client_email')
    total_orders = serializers.SerializerMethodField('get_client_total_orders')

    class Meta: 
        model = Client
        fields = '__all__'
        
    def get_client_email(self, client):
        return client.user.email
    
    def get_client_total_orders(self, client):
        return client.createorder_set.all().count()


    
    

