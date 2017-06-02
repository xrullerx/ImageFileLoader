from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    models = Image
    list_display = ('name', 'description', 'image', )
    list_filter = ('name',)


admin.site.register(Image, ImageAdmin)