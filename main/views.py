from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect, render
from main.models import *
from main.forms import (
    ProjectForm, 
    ExperienceForm, 
    ExperienceUpdateForm,
)    
import datetime





def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Hafizuddin Dzaki Azzam",
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Hafizuddin Dzaki Azzam",
        "npm": "2506597220",
        "study_program": "Computer Science Undergrad",
        "bio": (
            "CS student at Universitas Indonesia for, a while now. " 
            "Loves to read, study, and create stuff (also plays a variety of games). " 
            "Well, welcome to this website, I guess..  "
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def show_experience(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Hafizuddin Dzaki Azzam",
        "title_query": title_query,
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)


def show_project(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Hafizuddin Dzaki Azzam",
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)


@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied

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


@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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


@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    query_set = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceUpdateForm(instance=query_set)

    if request.method == "POST":
        form = ExperienceUpdateForm(request.POST or None, instance=query_set)
        if form.is_valid():
            form.save()
            messages.success(request, "Experience succesfully updated!")
            return redirect("main:show_experience")

    context = {
            "name": "Hafizuddin Dzaki Azzam",
            "form": form,
            "experience": query_set,
        }
    return render(request, "experience_update_form.html", context)


@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project succesfully deleted!")
        return redirect("main:show_project")

    return redirect("main:show_project")


@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience succesfully deleted!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")


def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "category": project.category,
                # "thumbnail": project.thumbnail,
                "created_at": project.created_at,
                "programs": project.programs,
                "link": project.link,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)


def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.prefetch_related('upvoted_by').all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences = sorted(experiences)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika 
    data = []
    for experience in experiences:
        upvoted_users = experience.upvoted_by.all()
        is_upvoted = request.user in upvoted_users if request.user.is_authenticated else False
        upvoted_by_names = ", ".join([u.username for u in upvoted_users])

        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.category,
                "skills": experience.skills,
                "started_at": experience.started_at,
                "ended_at": experience.ended_at,
                "is_ongoing": experience.is_ongoing,
                "upvote_count": upvoted_users.count(),
                "is_upvoted": is_upvoted,
                "upvoted_by_names": upvoted_by_names,
            }
        })

    return JsonResponse(data, safe=False)


@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_project")


@login_required(login_url="/login/")
def toggle_upvote(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.upvoted_by.all():
            experience.upvoted_by.remove(request.user)
        else:
            experience.upvoted_by.add(request.user)

    return redirect("main:show_experience")


@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Project added successfully.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan experience."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Experience added successfully.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)