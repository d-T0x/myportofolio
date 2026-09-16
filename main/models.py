import uuid
from django.db import models


class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    skills = models.TextField(blank=True, null=True)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None


class Project(models.Model):
    PROJECT_TYPE = [
            ('misc', 'Misc'),
            ('game', 'Game'),
            ('web', 'Web'),
            ('app', 'App'),
        ]
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=PROJECT_TYPE, default='misc')
    thumbnail = models.ImageField(blank=True, default="PlaceholderThumbnail.png")
    created_at = models.DateField()
    programs = models.TextField()
    link = models.URLField()
    def __str__(self):
        return self.title

    @property
    def exist_thumbnail(self):
        return self.thumbnail