import uuid

from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _


class Tenant(TenantMixin):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    tenant_key = models.CharField(max_length=50, unique=True)
    tenant_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tenant_name


class TenantUserManager(BaseUserManager):
    def create_user(self, username, tenant, password=None):
        if not username:
            raise ValueError('Requierd Username')

        user = self.model(
            username=username,
            tenant=tenant,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, tenant, password=None):
        user = self.model(
            username=username,
            tenant=tenant,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class TenantUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True)
    username = models.CharField(_("username"), max_length=150, unique=True)

    is_active = models.BooleanField(_("isActive"), default=True)
    is_admin = models.BooleanField(_("isAdmin"), default=False)
    is_staff = models.BooleanField(_("isStaff"), default=False)

    objects = TenantUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    filter_horizontal = ('username',)
    list_display = ('username',)
    list_filter = ('username',)


class Domain(DomainMixin):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    def __str__(self):
        return self.domain
