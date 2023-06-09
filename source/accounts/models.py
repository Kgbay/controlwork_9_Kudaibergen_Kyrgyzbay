from django.contrib.auth.models import AbstractUser, UserManager
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import TextChoices


class SexChoice(TextChoices):
    MALE = ('Male', 'Мужской')
    FEMALE = ('Female', 'Женский')


def validate_digits(value):
    if not value.isdigit():
        raise ValidationError('Телефон номера должен содержать только цифры')


class Account(AbstractUser):
    username = models.CharField(max_length=30, null=False, unique=True, verbose_name='Username')
    email = models.EmailField(verbose_name='Электронная почта', unique=True, blank=True, null=False)
    phone_number = models.CharField(
        max_length=11,
        verbose_name='Номер телефона',
        null=False,
        validators=[MinLengthValidator(11), validate_digits],
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars',
        verbose_name='Аватар',
        default='avatars/no_image.png'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    object = UserManager()

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'