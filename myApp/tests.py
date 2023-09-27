from django.test import TestCase
from django import http
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Blog, comment
from .forms import NewUserForm

class YourAppTestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a test blog
        self.blog = Blog.objects.create(
            author=self.user,
            title='Test Blog',
            content='This is a test blog.'
        )

        # Create a test client
        self.client = Client()

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_create_blog_view(self):
        # Login the user
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('createBlog'))
        self.assertEqual(response.status_code, 200)

    def test_show_blogs_view(self):
        response = self.client.get(reverse('showBlogs'))
        self.assertEqual(response.status_code, 200)

    def test_blog_page_view(self):
        response = self.client.get(reverse('blogPage', args=[self.blog.id]))
        self.assertEqual(response.status_code, 200)

    def test_add_comment_view(self):
        # Login the user
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('addComment', args=[self.blog.id]), {'comment': 'Test Comment'})
        self.assertEqual(response.status_code, 302)  # Redirects to the blog page

    def test_edit_blog_view(self):
        # Login the user
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('editBlog', args=[self.blog.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_blog_view(self):
        # Login the user
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('deleteBlog', args=[self.blog.id]))
        self.assertEqual(response.status_code, 302)  # Redirects to showBlogs

    def test_logout_request_view(self):
        # Login the user
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirects to login

    def test_valid_registration(self):
        form_data = {
            'username': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword',
        }
        form = NewUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_registration(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'wrongpassword',
        }
        form = NewUserForm(data=form_data)
        self.assertFalse(form.is_valid())

