from django.shortcuts import render
from .models import User, Project

# Create your views here.
def index(request):
        projects = Project.objects.all()
        user = User.objects.get(id=1)
        return render(request, 'home.html', {
                "projects": projects,
                "user": user
        })