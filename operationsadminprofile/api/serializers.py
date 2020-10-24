from rest_framework import serializers

from operationsadminprofile.models import OperationsAdminProfile


class OperationsAdminProfileSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField('get_username')
    email = serializers.SerializerMethodField('get_user_email')

    class Meta: 
        model = OperationsAdminProfile
        fields = ['id','username', 'email', 'phone', 'profile_photo', 'status']
    

    def get_username(self, operations_admin_profile):
        return operations_admin_profile.user.username

    def get_user_email(self, operations_admin_profile):
        return operations_admin_profile.user.email
        
    

