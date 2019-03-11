from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class LoginTests(TestCase):
    def test_contact_list_no_login(self):
        url = reverse('contactList:contacts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_contact_list_login(self):
        #create and log user in
        user = User.objects.create_user('test', 'test@test.com','somepassword')
        self.client.login(username='test',password='somepassword')
        url = reverse('contactList:contacts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
