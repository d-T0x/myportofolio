from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import *


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
            started_at="2024-10-20",
        )
        self.project = Project.objects.create(
            title="Project 1",
            description="dummy game",
            category = "game",
            created_at = "2026-05-05",
            programs = "godot",
            link = "https://example.com/",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

        data_response = self.client.get(reverse("main:get_experiences_json"))
        self.assertEqual(data_response.status_code, 200)
        experience = data_response.json()[0]["fields"]
        self.assertEqual(experience["title"], self.experience.title)
        self.assertEqual(experience["description"], self.experience.description)
        self.assertEqual(experience["category"], self.experience.category)
        self.assertTrue(experience["is_ongoing"])

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Under Construction!")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.localdate()
        self.experience.save()

        self.assertFalse(self.experience.is_ongoing)
        response = self.client.get(reverse("main:get_experiences_json"))
        experience = response.json()[0]["fields"]
        self.assertEqual(experience["ended_at"], self.experience.ended_at.isoformat())
        self.assertFalse(experience["is_ongoing"])

    def test_project_model(self):
            self.assertEqual(str(self.project), "Project 1")
            self.assertEqual(self.project.category, "game")
            self.assertEqual(self.project.programs, "godot")
    
    def test_project_page(self):
        response = self.client.get(reverse("main:show_project"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

        data_response = self.client.get(reverse("api:project-list"))
        self.assertEqual(data_response.status_code, 200)
        project = data_response.json()[0]
        self.assertEqual(project["title"], self.project.title)
        self.assertEqual(project["description"], self.project.description)
        self.assertEqual(project["category"], self.project.category)
        self.assertEqual(project["programs"], self.project.programs)
        self.assertEqual(project["link"], self.project.link)

    def test_empty_project_page(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("main:show_project"))

        self.assertContains(response, "Under Construction!")