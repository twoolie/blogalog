"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class BlogalogViewsTest(TestCase):
    fixtures = ['blogalog-01-testdata.json']

    def test_index(self):
        """
        Test the index view, which lists our most recent, visible, posts.
        """
        resp = self.client.get('/blog/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('latest_blog_entries' in resp.context)
        self.assertEqual([entry.pk for entry in resp.context['latest_blog_entries']], [2, 1])
        entry_1 = resp.context['latest_blog_entries'][1]
        self.assertEqual(entry_1.title, 'Test entry ')

    def test_detail(self):
        """
        Test the detail view
        """ 
        resp = self.client.get('/blog/entry/1')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['entry'].pk, 1)
        #Ensure that non-existant polls make a 404 happen!
        resp = self.client.get('/blog/entry/3')
        self.assertEqual(resp.status_code, 404)
