from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from .forms import RegistrationForm


class UserFormTest(TestCase):
    def test_user_form_invalid(self):
        form = RegistrationForm(data={'username': '', 'email': 'something', 'password1': '', 'password2': 'something'})
        self.assertFalse(form.is_valid())


class LoginRequestViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='test_user1', password='12345')
        test_user.save()

    def test_user_login(self):
        login = self.client.login(username='test_user1', password='12345')
        resp = self.client.get(reverse('shop:base'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(str(resp.context['user']), 'test_user1')