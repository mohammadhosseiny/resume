import os
import random

from django.db import models


def get_file_basename(basename):
    basename1 = os.path.basename(basename)
    name, ext = os.path.splitext(basename1)
    return name, ext


def get_image_path(instance, filename):
    new_name = random.randint(1, 1324328765)
    name, ext = get_file_basename(filename)
    origin_name = f'{new_name}{ext}'
    return f'products/{origin_name}'


class PortfolioManager(models.Manager):
    def get_all_info(self):
        return self.get_queryset().all()


class PortfolioManage(models.Model):
    name = models.CharField(null=False, blank=False, max_length=120, verbose_name='Full Name')
    skill1 = models.CharField(null=False, blank=True, max_length=120, verbose_name='First Skill')
    skill2 = models.CharField(null=False, blank=True, max_length=120, verbose_name='Second Skill')
    skill3 = models.CharField(null=False, blank=True, max_length=120, verbose_name='Third Skill')
    skill4 = models.CharField(null=False, blank=True, max_length=120, verbose_name='Fourth Skill')
    prof_img = models.ImageField(upload_to=get_image_path, null=False, blank=False, verbose_name='Profile Image')
    background_img = models.ImageField(upload_to=get_image_path, null=False, blank=False,
                                       verbose_name='Background Image')
    linkedin_link = models.URLField(max_length=120, null=True, blank=False, verbose_name='Social Media (Linkedin)')
    instagram_link = models.URLField(max_length=120, null=True, blank=False, verbose_name='Social Media (Instagram)')
    telegram_link = models.URLField(max_length=120, null=True, blank=False, verbose_name='Social Media (Telegram)')

    def get_all(self):
        return self.objects.all()

    object = PortfolioManager

    def __str__(self):
        return self.name


class PortfolioManage_Fa(models.Model):
    name = models.CharField(null=False, blank=False, max_length=120, verbose_name='نام کامل')
    skill1 = models.CharField(null=False, blank=True, max_length=120, verbose_name='مهارت اول')
    skill2 = models.CharField(null=False, blank=True, max_length=120, verbose_name='مهارت دوم')
    skill3 = models.CharField(null=False, blank=True, max_length=120, verbose_name='مهارت سوم')
    skill4 = models.CharField(null=False, blank=True, max_length=120, verbose_name='مهارت چهارم')
    prof_img = models.ImageField(upload_to=get_image_path, null=False, blank=False, verbose_name='تصویر پروفایل')
    background_img = models.ImageField(upload_to=get_image_path, null=False, blank=False,
                                       verbose_name='تصویر پس زمینه')
    linkedin_link = models.URLField(max_length=120, null=True, blank=False, verbose_name='Social Media (Linkedin)')
    instagram_link = models.URLField(max_length=120, null=True, blank=False, verbose_name='Social Media (Instagram)')
    telegram_link = models.URLField(max_length=120, null=True, blank=False, verbose_name='Social Media (Telegram)')

    def get_all(self):
        return self.objects.all()

    object = PortfolioManager

    def __str__(self):
        return self.name
