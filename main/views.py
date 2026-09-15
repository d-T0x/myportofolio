from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import *
from main.forms import ProjectForm


def show_main(request):
    context = {
        "name": "Hafizuddin Dzaki Azzam",
        "npm": "2506597220",
        "study_program": "Computer Science Undergrad",
        "bio": (
            "CS student at Universitas Indonesia for, a while now. " 
            "Loves to read, study, and create stuff (also plays a variety of games). " 
            "Well, welcome to this website, I guess..  "
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Hafizuddin Dzaki Azzam",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def show_project(request):
    context = {
        "name": "Hafizuddin Dzaki Azzam",
        "project_list": Project.objects.all(),
    }
    return render(request, "project.html", context)


def create_project(request):
    form = ProjectForm(request.POST, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "A new project has been added!")
        return redirect("main:show_project")

    context = {
        "name": "Hafizuddin Dzaki Azzam",
        "form": form,
    }
    return render(request, "projects_form.html", context)