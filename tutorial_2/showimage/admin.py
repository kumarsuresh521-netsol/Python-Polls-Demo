from django.contrib import admin

# Register your models here.
from showimage.models import ShowImage
# Register your models here.

class ShowImageAdmin(admin.ModelAdmin):
    list_display = ['image_name', 'image_src']
    ordering = ['image_name']

    
admin.site.register(ShowImage, ShowImageAdmin)