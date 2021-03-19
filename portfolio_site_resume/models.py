import os
import random

from django.db import models


# Create your models here.


def get_file_basename(basename):
    basename1 = os.path.basename(basename)
    name, ext = os.path.splitext(basename1)
    return name, ext


def get_image_path(instance, filename):
    new_name = random.randint(1, 1324328765)
    name, ext = get_file_basename(filename)
    origin_name = f'{new_name}{ext}'
    return f'resume/{origin_name}'


class SiteResume(models.Model):
    title = models.CharField(max_length=120, verbose_name='Site Name')
    siteurl = models.URLField(max_length=120, verbose_name='Site Url')
    image = models.ImageField(upload_to=get_image_path, verbose_name='Site Image', null=True, blank=False)

    def __str__(self):
        return self.title

