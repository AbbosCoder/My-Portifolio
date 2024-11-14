# myportfolio/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # related_name ni o'zgartiramiz
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # related_name ni o'zgartiramiz
        blank=True
    )
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)], default=5)

    def __str__(self):
        return self.name

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experiences')
    company_name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.company_name} - {self.position}"

class ContactInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email

class SocialMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_media')
    platform_name = models.CharField(max_length=100)  # LinkedIn, GitHub va boshqalar
    link = models.URLField()

    def __str__(self):
        return f"{self.platform_name} - {self.link}"
