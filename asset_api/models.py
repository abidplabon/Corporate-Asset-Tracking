from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.utils import timezone


# Company Profile Creating Model
class CompanyProfileManager(BaseUserManager):
    """Create a company's profile"""

    def create_user(self, email, name, password: None):
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class CompanyProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for the user companies """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CompanyProfileManager()

    USERNAME_FIELD = 'email'  # override the default main field from name to email
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.email


# Which attributes should be selected for taking employee records
class EmployeeRecord(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=255)
    device_name = models.CharField(max_length=255, null=True)
    allocation_start_date = models.DateField(default=timezone.now)
    allocation_end_date = models.DateField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True)
    return_on = models.DateTimeField(max_length=255)
    allocation_condition = models.CharField(max_length=255, null=True)
    return_condition = models.CharField(max_length=255, null=True)
    asset_issued = models.BooleanField(default=False)

    def __str__(self):
        return self.employee_name
