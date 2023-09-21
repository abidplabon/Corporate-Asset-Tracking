from rest_framework import serializers
from asset_api import models
from asset_api.models import EmployeeRecord


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)


# Create company profile with ID, Email, Name, Password
class CompanyProfileSerializer(serializers.ModelSerializer):
    """Serializer for a company object"""

    class Meta:
        model = models.CompanyProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}  # Hide the password while typing
            }
        }

    def create(self, validated_data):
        user = models.CompanyProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


# Get all the records of employees from Employee Model
class EmployeeRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRecord
        fields = '__all__'
        read_only_fields = ('id', 'created_on')
