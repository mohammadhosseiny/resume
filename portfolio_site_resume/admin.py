from django.contrib import admin

# Register your models here.
from portfolio_site_resume.models import SiteResume


class SiteResume_ListDisplay(admin.ModelAdmin):
    list_display = ['__str__']


admin.site.register(SiteResume, SiteResume_ListDisplay)