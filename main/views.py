from django.shortcuts import render
from main.models import Experience


def show_main(request):
    context = {
        "name": "Hafizuddin Dzaki Azzam",
        "npm": "2506597220",
        "study_program": "Computer Science Undergrad",
        "bio": (
            "CS student at Universitas Indonesia for, a while now." 
            "Loves to read, study, and create stuff (also plays a variety of games)." 
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