from django.contrib import admin
from .models import Image

class ImageAdmin(admin.ModelAdmin):
    fields = ('image', 'note')

admin.site.register(Image, ImageAdmin)
