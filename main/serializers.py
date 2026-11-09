from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Project, Experience


class ProjectSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id", "title", "description", "category",
            "created_at", "programs", "link", "starred_by",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id", "starred_by"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_tech_stack(self, value):
        return strip_tags(value)

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())


class ExperienceSerializer(serializers.ModelSerializer):
    upvote_count = serializers.SerializerMethodField()
    is_upvoted = serializers.SerializerMethodField()
    upvoted_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            "id", "title", "description", "category",
            "skills", "started_at", "ended_at", "is_ongoing",
            "upvote_count", "is_upvoted", "upvoted_by_names",
        ]
        read_only_fields = ["id", "is_ongoing"]

    def validate(self, data):
        valid = True
        start_date = data['started_at']
        end_date = data['ended_at']
        if end_date and start_date and end_date < start_date:
            serializers.ValidationError('End date must be greater than start date')
            valid = False
        return valid

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Experience name can't be only HTML tag.")
        return value
    
    def validate_description(self, value):
        return strip_tags(value)

    def validate_category(self, value):
        return strip_tags(value)

    def get_upvote_count(self, obj):
        return obj.upvoted_by.count()

    def get_is_upvoted(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.upvoted_by.all()
    
    def get_upvoted_by_names(self, obj):
        return ", ".join(user.username for user in obj.upvoted_by.all())

    def get_is_ongoing(self, obj):
        return obj.is_ongoing