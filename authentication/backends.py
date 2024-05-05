from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http import HttpRequest

UserModel = get_user_model()

class EmailAuthBackend(BaseBackend):
    def authenticate(self, request: HttpRequest, email: str | None, password: str | None) -> AbstractBaseUser | None:
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None
        

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None