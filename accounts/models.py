from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class Bidang(models.Model):
    bidang_id = models.IntegerField()
    nama_bidang = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_bidang


class Role(models.Model):
    role_id = models.IntegerField()
    bidang = models.ForeignKey(Bidang, on_delete=models.CASCADE)
    is_kabid = models.BooleanField(default=False)
    nama_role = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_role


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('User harus mempunyai email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    user_id = models.CharField(max_length=8)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
