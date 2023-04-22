from django.contrib import admin
from .models import Image

class ImageAdmin(admin.ModelAdmin):
    fields = ('image', 'note', 'user')

admin.site.register(Image, ImageAdmin)
