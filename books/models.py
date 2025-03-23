from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)  
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email=email, password=password, **extra_fields)

class AdminUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = None  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="admin_users",  
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="admin_users_permissions",  
        blank=True,
    )

    objects = CustomUserManager()


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()

    def __str__(self):
        return self.title
