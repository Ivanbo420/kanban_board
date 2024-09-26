from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    # Add the related_name argument to resolve the clashes
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Use a unique related_name for the reverse relationship
        blank=True,
        help_text='The groups this user belongs to.'
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set_permissions',  # Use a unique related_name for the reverse relationship
        blank=True,
        help_text='Specific permissions for this user.'
    )

