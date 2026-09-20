from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import *
from main.forms import ProjectForm, ExperienceForm


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
    json_response = get_experiences_json(request)
    
    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Hafizuddin Dzaki Azzam",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)


def show_project(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Hafizuddin Dzaki Azzam",
        "project_list": projects,
        "title_query": title_query,
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


def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "A new experience has been added!")
        return redirect("main:show_experience")

    context = {
        "name": "Hafizuddin Dzaki Azzam",
        "form": form,
    }
    return render(request, "experience_form.html", context)


def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project succesfully deleted!")
        return redirect("main:show_project")

    return redirect("main:show_project")


def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience succesfully deleted!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")



def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")


def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")