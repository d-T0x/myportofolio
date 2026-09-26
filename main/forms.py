from django.forms import (
    ModelForm, 
    TextInput, 
    Textarea, 
    Select, 
    URLInput,
    DateInput,
    ModelMultipleChoiceField,
)
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple    
from django.contrib.auth.models import Group


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
                    "placeholder": "27 February 2020",
                }
            ),
            "ended_at": DateInput(
                attrs={
                    "placeholder": "1 March 2020. Leave empty if ongoing",
                }
            ),
        }

    def is_valid(self):
        valid = super().is_valid()

        if hasattr(self, 'cleaned_data') and valid:
            start_date = self.cleaned_data.get('started_at')
            end_date = self.cleaned_data.get('ended_at')
            if end_date and start_date and end_date < start_date:
                self.add_error('ended_at', 'End date must be greater than start date')
                valid = False

        return valid


class ExperienceUpdateForm(ModelForm):
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
                        "placeholder": "27 February 2020",
                    }
                ),
                "ended_at": DateInput(
                    attrs={
                        "placeholder": "1 March 2020. Leave empty if ongoing",
                    }
                ),
            }

    def is_valid(self):
        valid = super().is_valid()

        if hasattr(self, 'cleaned_data') and valid:
            start_date = self.cleaned_data.get('started_at')
            end_date = self.cleaned_data.get('ended_at')
            if end_date and start_date and end_date < start_date:
                self.add_error('ended_at', 'End date must be greater than start date')
                valid = False

        return valid


user = get_user_model()
# Create ModelForm based on the Group model.
class GroupAdminForm(ModelForm):
    class Meta:
        model = Group
        exclude = []

    # Add the users field.
    users = ModelMultipleChoiceField(
         queryset=user.objects.all(), 
         required=False,
         # Use the pretty 'filter_horizontal widget'.
         widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance
