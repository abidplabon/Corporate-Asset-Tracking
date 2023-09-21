from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from asset_api import models, permissions
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from asset_api import serializer
from asset_api.models import EmployeeRecord
from asset_api.serializer import EmployeeRecordSerializer
from rest_framework.permissions import IsAuthenticated


# Giving basic vision of the working of the API where for fun you can put your name to get greeting from the API
class HelloAPI(APIView):
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            "The API Registers different companies",
            "Company can add, edit, delete their employees asset records",
            "Particular date time of return can be assigned to each record",
        ]
        return Response({'message': 'Hello', 'an_api': an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})


# Testing API
class HelloView(viewsets.ViewSet):
    def list(self, request):
        viewset = [
            'Contributor : Md.Abid Ahammed',
            'Email : abid15@cse.pstu.ac.bd'
        ]
        return Response({'message': 'Hello!!!!', 'viewset': viewset})


# Making a user company (Register)
class CompanyProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.CompanyProfileSerializer
    queryset = models.CompanyProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


# Making a registered company login
class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# Assigning employee device and taking records with time and condition
class EmployeeRecordViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.EmployeeEdit, IsAuthenticated)
    serializer_class = EmployeeRecordSerializer
    queryset = EmployeeRecord.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        # Filter the queryset to show only records owned by the logged-in user.
        return EmployeeRecord.objects.filter(owner=self.request.user)
