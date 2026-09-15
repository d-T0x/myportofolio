#from django.forms import ModelForm, TextInput, Textarea, URLInput
from django.forms import *
from main.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "created_at",
            "programs",
            "link",
        ]

        labels = {
            "title": "Project's Name",
            "description": "Project's Description",
            "category": "Project Type",
            "thumbnail": "Project's Thumbnail",
            "created_at": "Date of Creation",
            "programs": "Programs Used in Development",
            "link": "Project's URL",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell about your website",
                    "rows": 3,
                }
            ),
            "category": Select(
                attrs={
                }
            ),
            "programs": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "link": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
        }