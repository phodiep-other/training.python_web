"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

from entry.models import Entry

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class EntryTest(TestCase):
    def setUp(self):
        self.expected_title = "title 1"
        self.expected_text = "text 1"
        User.objects.create_user('testname', 'test@email.com', 'testpassword')
        self.expected_author = User.objects.get(username='testname')
        self.entry = Entry.objects.create(
            title = self.expected_title,
            text = self.expected_text,
            author = self.expected_author,
            pub_date = timezone.now())

    def test_title_display(self):
        self.assertEquals(self.entry.title, self.expected_title)
        new_title = "title A"
        self.entry.title = new_title
        self.assertEquals(self.entry.title, new_title)

    def test_text_display(self):
        self.assertEquals(self.entry.text, self.expected_text)
        new_text = "text A"
        self.entry.text = new_text
        self.assertEquals(self.entry.text, new_text)

    def test_author_display(self):
        self.assertEquals(self.entry.author, self.expected_author)
        User.objects.create_user('AAA', 'BBB', 'CCC')
        new_author = User.objects.get(username='AAA')
        self.entry.author = new_author
        self.assertEquals(self.entry.author, new_author)

    def test_published_today(self):
        self.assertTrue(self.entry.published_today())
        delta = timedelta(hours=26)
        self.entry.pub_date = self.entry.pub_date - delta
        self.assertFalse(self.entry.published_today())

        
