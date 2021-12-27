import uuid

from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.utils import timezone


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and saves a new user"""
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and saves a new user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    guid = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_restaurant = models.BooleanField(default=False)
    meta = models.JSONField(null=True)
    date_joined = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "users"

    objects = UserManager()

    USERNAME_FIELD = "email"
