from django.contrib.auth.models import (
     BaseUserManager
)


class UserManager(BaseUserManager):
    use_in_migrations: True

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('Email is require')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError(('Super user must have is_staff true'))

        return self.create_user(email, password , **extra_fields)