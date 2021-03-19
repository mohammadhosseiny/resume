from django.contrib import admin

# Register your models here.
from portfolio_about.models import AboutSection, Skill, AboutSection_Fa

admin.site.register(AboutSection)
admin.site.register(AboutSection_Fa)

admin.site.register(Skill)
