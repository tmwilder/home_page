"""
Contains tests for the home page landing point.
Since the app is small, all tests are lumped in here.

"""
from django.test import TestCase, Client


class TestHomePageApp(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = Client()

    def test_main(self):
          response = self.c.get("/home")
          self.assertEqual(response.status_code, 200)
          self.assertEqual(response.templates[0].name, "main.html")

    def test_contact(self):
        response = self.c.post("/contact")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, "main.html")
