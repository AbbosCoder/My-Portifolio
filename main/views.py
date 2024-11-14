# myportfolio/views.py
from django.shortcuts import render
from .models import User,Skill,SocialMedia,Experience,ContactInfo,Project

def home(request):
    user = User.objects.first()  # Faqat bitta user borligi uchun
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    contacts = ContactInfo.objects.all()
    social_media = SocialMedia.objects.all()

    context = {
        'user': user,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'contacts': contacts,
        'social_media': social_media,
    }
    return render(request, 'home.html', context)
