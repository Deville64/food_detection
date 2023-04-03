from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from food_detection.forms import LoginForm

class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
    
    def test_login_successful(self):
        form_data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
    
    def test_login_invalid_credentials(self):
        form_data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 200)
    
    def test_login_invalid_form(self):
        form_data = {'username': '', 'password': ''}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        
        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 200)
