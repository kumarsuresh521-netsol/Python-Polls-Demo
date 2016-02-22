from __future__ import unicode_literals
from django.db import models

# Create your models here.

class ShowImage(models.Model):
    image_name = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to="", default='')
    
    def image_src(self):
        return u' <a href="http://127.0.0.1:8000/media/%s" target="_blank"><img style=" height:80px;" src="http://127.0.0.1:8000/media/%s" alt="%s" /></a> ' % \
                          (self.image_url, self.image_url, self.image_name)
    image_src.short_description = 'Image'
    image_src.allow_tags = True