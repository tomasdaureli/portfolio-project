from django.db import models
from django.db.models.fields import CharField, URLField, EmailField

# Create your models here.
class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    link = URLField(blank=True)

class User(models.Model):
    name = CharField(max_length=100)
    job = CharField(max_length=100)
    bio = CharField(max_length=1000)
    knowledge = CharField(max_length=1000)
    email = EmailField(max_length=255)
    github = URLField(blank=True)
    linkedin = URLField(blank=True)