# myportfolio/admin.py
from django.contrib import admin
from .models import User, Skill, Project, Experience, ContactInfo, SocialMedia

admin.site.register(User)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(ContactInfo)
admin.site.register(SocialMedia)
