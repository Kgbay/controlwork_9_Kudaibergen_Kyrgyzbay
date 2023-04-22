from django.conf import settings
from django.db import models

from .images import Image


class Favorite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='favorite_images',
        verbose_name='Избранное',
        null=False,
        on_delete=models.CASCADE
    )
    image = models.ForeignKey(
        to=Image,
        related_name='favorite_images',
        verbose_name='Избранное',
        null=False,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Избранное изображение',
        verbose_name_plural = 'Избранные изображения'
