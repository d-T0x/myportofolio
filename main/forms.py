from django.forms import (
    ModelForm, 
    TextInput, 
    Textarea, 
    Select, 
    URLInput,
    DateInput,
)
from main.models import (
    Project,
    Experience,
)

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


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "skills",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Position/Title/Name",
            "description": "Experience Description",
            "category": "Experience Type",
            "skills": "Skills",
            "started_at": "Starting Date",
            "ended_at": "End Date",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Lead of XXX",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "What did you do?",
                    "rows": 3,
                }
            ),
            "skills": Textarea(
                attrs={
                    "placeholder": "Creative thinking, team work, etc.",
                    "rows": 3,
                }
            ),
            "started_at": DateInput(
                attrs={
                    "placeholder": "29 February 2020",
                }
            ),
            "ended_at": DateInput(
                attrs={
                    "placeholder": "1 March 2020",
                }
            ),
        }