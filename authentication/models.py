from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from setuptools._entry_points import _


class UserManager(BaseUserManager):
    def create_user(self, name, email,
                    school_id, password=None):
        user = self.model(
            school_id=school_id,
            email=self.normalize_email(email),
            name=name,

        )
        # user.is_administrator = is_administrator
        # user.is_manager = is_manager
        # user.is_member = is_member
        # user.is_manager_and_member = is_manager_and_member
        print(password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user_no_password(self, name, email,
                                school_id):
        user = self.model(
            school_id=school_id,
            email=self.normalize_email(email),
            name=name,

        )
        # user.is_administrator = is_administrator
        # user.is_manager = is_manager
        # user.is_member = is_member
        # user.is_manager_and_member = is_manager_and_member

        user.save(using=self._db)
        return user

    # def create_staffuser(self, email, password):
    #     user = self.create_user(
    #         email,
    #         password=password,
    #     )
    #     user.staff = True
    #     user.save(using=self._db)
    #     return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            school_id="0000000",
            name="SuperUser",
            # is_administrator=False,
            # is_manager=False,
            # is_member=False,
            # is_manager_and_member=False,
            password=password,

        )
        user.is_superuser = True
        user.staff = True
        user.admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    school_id = models.CharField(max_length=7, unique=True)
    name = models.CharField(max_length=100)

    password = models.CharField(null=True, blank=True, max_length=128)
    email = models.EmailField(unique=True, max_length=255)
    # is_administrator = models.BooleanField(default=False)
    # is_manager = models.BooleanField(default=False)  # a admin user; non super-user
    # is_member = models.BooleanField(default=False)
    # is_manager_and_member = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def get_id(self):
        return self.id

    def get_full_name(self):
        return self.name

    def get_email(self):
        return self.email

    def __str__(self):
        return str(self.school_id) + ", " + self.email

#
# class Member(User):
#     grade_level = models.IntegerField()
#
#     class Meta:
#         verbose_name = 'Member'
#
#
# class Sponsor(User):
#     class Meta:
#         verbose_name = 'Sponsor'
#
#
# class Officer(User):
#     grade_level = models.IntegerField()
#
#     class Meta:
#         verbose_name = 'Officer'
#

class Administrator(User):
    class Meta:
        verbose_name = 'Administrator'


class TitleImage(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='')

    def __str__(self):
        return self.image.name
