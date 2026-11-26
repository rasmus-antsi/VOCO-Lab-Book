from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user from day one so fields (role, strikes) can be added without resetting the database."""
