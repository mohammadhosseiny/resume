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
    return f'products/{origin_name}'


class AboutSection(models.Model):
    about_me = models.CharField(max_length=200, null=True, blank=False, verbose_name='About Me')
    about_me2 = models.CharField(max_length=200, null=True, blank=False, verbose_name='About Me 2')
    image = models.ImageField(upload_to=get_image_path, null=True, blank=False, verbose_name='Image')
    skill = models.CharField(max_length=130, null=False, blank=False, verbose_name='My Primary Skills')
    birthday = models.DateField(null=False, blank=False, verbose_name='MY BirthDay')
    website = models.URLField(max_length=130, null=False, blank=True, verbose_name='My Website')
    phone = models.CharField(max_length=20, null=False, blank=False, verbose_name='Phone Number')
    city = models.CharField(max_length=60, null=False, blank=False, verbose_name='City')
    age = models.IntegerField(null=False, blank=False, verbose_name='Age')
    degree = models.CharField(max_length=60, null=False, blank=False, verbose_name='Degree')
    email = models.EmailField(max_length=60, null=False, blank=False, verbose_name='Email')
    freelance = models.BooleanField(default=False, null=False, blank=False,
                                    verbose_name='Freelance :Available/unAvailable')


class AboutSection_Fa(models.Model):
    about_me = models.CharField(max_length=200, null=True, blank=False, verbose_name='About Me')
    about_me2 = models.CharField(max_length=200, null=True, blank=False, verbose_name='About Me 2')
    image = models.ImageField(upload_to=get_image_path, null=True, blank=False, verbose_name='Image')
    skill = models.CharField(max_length=130, null=False, blank=False, verbose_name='My Primary Skills')
    birthday = models.DateField(null=False, blank=False, verbose_name='MY BirthDay')
    website = models.URLField(max_length=130, null=False, blank=True, verbose_name='My Website')
    phone = models.CharField(max_length=20, null=False, blank=False, verbose_name='Phone Number')
    city = models.CharField(max_length=60, null=False, blank=False, verbose_name='City')
    age = models.IntegerField(null=False, blank=False, verbose_name='Age')
    degree = models.CharField(max_length=60, null=False, blank=False, verbose_name='Degree')
    email = models.EmailField(max_length=60, null=False, blank=False, verbose_name='Email')
    freelance = models.BooleanField(default=False, null=False, blank=False,
                                    verbose_name='Freelance :Available/unAvailable')


class Skill(models.Model):
    title = models.CharField(max_length=50, null=True, blank=False, verbose_name='Skill Title')
    progress = models.IntegerField(null=True, blank=False, verbose_name='Progress (%)')

    def __str__(self):
        return self.title
