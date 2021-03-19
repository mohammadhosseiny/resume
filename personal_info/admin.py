from django.contrib import admin


# Register your models here.
from personal_info.models import PortfolioManage, PortfolioManage_Fa


class Portfolio_Manager(admin.ModelAdmin):
    list_display = ['__str__', 'skill1', 'skill2', 'skill3', 'skill4']
    list_editable = ['skill1', 'skill2', 'skill3', 'skill4']

    class Meta:
        model = PortfolioManage


admin.site.register(PortfolioManage, Portfolio_Manager)
admin.site.register(PortfolioManage_Fa, Portfolio_Manager)
