from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_groups',  # Add related_name to resolve clash
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_permissions',  # Add related_name to resolve clash
        help_text=_('Specific permissions for this user.'),
    )

    permissions = [
        ("authentication_add_user", "Can add user"),
        ("authentication_change_user", "Can change user"),
        ("authentication_delete_user", "Can delete user"),
        ("authentication_view_user", "Can view user"),
    ]

    class Meta:
        permissions = [
            ("authentication_add_user", "Can add user"),
            ("authentication_change_user", "Can change user"),
            ("authentication_delete_user", "Can delete user"),
            ("authentication_view_user", "Can view user"),
        ]
    
        