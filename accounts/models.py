# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from .managers import CustomUserManager

# # Create your models here.


# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(unique=True)
#     age = models.PositiveIntegerField(null=True, blank=True)
#     avatar = models.ImageField(upload_to="uploads/profileImage/", null=True)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["avatar"]

#     # objects = CustomUserManager()

#     def __str__(self):
#         return self.email
