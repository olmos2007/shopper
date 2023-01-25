from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import integer_validator
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class Product(models.Model):
    class ChoiceSize(models.TextChoices):
        XS = 'xs'
        X = 'x'
        M = 'm'
        L = 'l'
        XL = 'xl'

    class ChoiceColor(models.TextChoices):
        BLACK = 'Black'
        WHITE = 'White'
        RED = 'Red'
        BLUE = 'Blue'
        GREEN = 'Green'

    image = models.ImageField(upload_to='product/')
    title = models.CharField(max_length=155)
    review = models.IntegerField(default=1, null=True, blank=True)
    price = models.FloatField()
    text = models.TextField()
    choice = models.CharField(max_length=55, choices=ChoiceSize.choices, default=ChoiceSize.XL)
    color = models.CharField(max_length=25, choices=ChoiceColor.choices, default=ChoiceColor.WHITE)
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey('app.Category', on_delete=models.CASCADE)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have a phone number!')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = models.CharField(max_length=155, unique=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=25, validators=[integer_validator], null=True, blank=True)
    address = models.CharField(max_length=155, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()




