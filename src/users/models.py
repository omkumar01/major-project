from django.db import models
from django.contrib.auth.models import BaseUserManager


class MyuserManager(BaseUserManager):

    def create_user(self, email, password = None):
        """
         creates abd saves a user with email, password.
        """
        if not email:
            raise ValueError("users must have email address")
        
        user = self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, password=None):
        pass
