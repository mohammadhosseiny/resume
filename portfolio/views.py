from django.shortcuts import render

from personal_info.models import PortfolioManage, PortfolioManage_Fa
from portfolio_about.models import AboutSection, Skill, AboutSection_Fa
from portfolio_site_resume.models import SiteResume


def home_page(request):
    siteresume: SiteResume = SiteResume.objects.all()
    about: AboutSection = AboutSection.objects.first()
    portfolio: PortfolioManage = PortfolioManage.objects.first()
    skills = Skill.objects.all()
    context = {
        'portfolio': portfolio,
        'about': about,
        'skills': skills,
        'siteresume': siteresume,
    }
    return render(request, 'home_page.html', context)


def home_page_fa(request):
    siteresume: SiteResume = SiteResume.objects.all()
    about: AboutSection_Fa = AboutSection_Fa.objects.first()
    portfolio: PortfolioManage_Fa = PortfolioManage_Fa.objects.first()
    skills = Skill.objects.all()
    context = {
        'siteresume': siteresume,
        'about': about,
        'portfolio': portfolio,
        'skills': skills,

    }
    return render(request, 'home_page_fa.html', context)
