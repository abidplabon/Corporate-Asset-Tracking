from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from asset_api import views

route = DefaultRouter()
route.register('viewHello', views.HelloView, basename='viewHello')
route.register('companyprofile', views.CompanyProfileViewSet, basename='CompanyProfileViewSet')
route.register('employee-records', views.EmployeeRecordViewSet, basename='employee-records')

urlpatterns = [
    path('hello-view', views.HelloAPI.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(route.urls))
]
