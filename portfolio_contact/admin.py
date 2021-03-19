from django.contrib import admin

# Register your models here.
from portfolio_contact.models import Contact


class ModelManager(admin.ModelAdmin):
    list_display = ['__str__', 'email']


admin.site.register(Contact, ModelManager)
