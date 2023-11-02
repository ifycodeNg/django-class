# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     fieldsets = (
#         (None, {"fields": ("email", "password", "avatar")}),
#         (
#             "permissions",
#             {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
#         ),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": (
#                     "email",
#                     "password1",
#                     "password2",
#                     "is_staff",
#                     "is_active",
#                     "groups",
#                     "user_permissions",
#                 ),
#             },
#         ),
#     )

#     list_display = ("email", "is_staff", "is_active")
#     ordering = ("email",)


# admin.site.register(CustomUser, CustomUserAdmin)
