from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from django_pjaxr.test_views import *


urlpatterns = patterns('',
    url(r'^page1/$',                                Page1View.as_view(),                    name='page_1'),
    url(r'^page1/content1/$',                       Page1Content1View.as_view(),            name='content_1'),
    url(r'^page1/content1/inner_content1/$',        Page1Content1View.as_view(),            name='inner_content_1'),
    url(r'^page1/content1/inner_content2/$',        Page1Content1View.as_view(),            name='inner_content_2'),
    url(r'^page1/content2/$',                       Page1Content2View.as_view(),            name='content_2'),
    url(r'^page2/$',                                Page2View.as_view(),                    name='page_2'),
)


class TestPjaxrRequests(TestCase):

    urls = 'django_pjaxr.tests'
    page_1_string = 'page_1'
    content_1_string = 'content_1'
    content_2_string = 'content_2'
    inner_content_1_string = 'inner_content_1'
    inner_content_2_string = 'inner_content_2'
    page_2_string = 'page_2'

    # testing with 1 namespace
    def test_test1_no_pjaxr(self):
        client = Client()
        response = client.get(reverse('page_1'))
        self.assertContains(response, self.page_1_string)
        self.assertNotContains(response, self.content_1_string)
        self.assertContains(response, '<html>')
        self.assertNotContains(response, '<pjaxr-body>')

    def test_test1_pjaxr_with_namespace(self):
        client = Client()
        response = client.get(reverse('page_1'), **{'HTTP_X_PJAX': 'true', 'HTTP_X_PJAX_NAMESPACE': 'Site1.Page2'})
        self.assertContains(response, self.page_1_string)
        self.assertNotContains(response, self.content_1_string)
        self.assertContains(response, '<pjaxr-body>')
        self.assertNotContains(response, '<html>')

    def test_test1_pjaxr_different_namespace(self):
        client = Client()
        response = client.get(reverse('page_1'), **{'HTTP_X_PJAX': 'true', 'HTTP_X_PJAX_NAMESPACE': 'Site2'})
        self.assertContains(response, self.page_1_string)
        self.assertNotContains(response, self.content_1_string)
        self.assertNotContains(response, '<pjaxr-body>')
        self.assertContains(response, '<html>')

    def test_test1_pjaxr_no_namespace(self):
        client = Client()
        response = client.get(reverse('page_1'), **{'HTTP_X_PJAX': 'true'})
        self.assertContains(response, self.page_1_string)
        self.assertNotContains(response, self.content_1_string)
        self.assertContains(response, '<pjaxr-body>')
        self.assertNotContains(response, '<html>')

    # testing with 2 hierarchically structured namespaces

    def test_test2_no_pjaxr(self):
        client = Client()
        response = client.get(reverse('content_1'))
        self.assertContains(response, self.page_1_string)
        self.assertContains(response, self.content_1_string)
        self.assertContains(response, '<html>')
        self.assertNotContains(response, '<pjaxr-body>')

    def test_test2_pjaxr_current_namespace(self):
        client = Client()
        response = client.get(reverse('content_1'), **{'HTTP_X_PJAX': 'true', 'HTTP_X_PJAX_NAMESPACE': 'Site1.Page1.Content1'})
        self.assertNotContains(response, self.page_1_string)
        self.assertNotContains(response, self.content_1_string)
        self.assertContains(response, '<pjaxr-body>')
        self.assertNotContains(response, '<html>')

    def test_test2_pjaxr_page_namespace(self):
        client = Client()
        response = client.get(reverse('content_1'), **{'HTTP_X_PJAX': 'true', 'HTTP_X_PJAX_NAMESPACE': 'Site1.Page1'})
        self.assertNotContains(response, self.page_1_string)
        self.assertContains(response, self.content_1_string)
        self.assertContains(response, '<pjaxr-body>')
        self.assertNotContains(response, '<html>')

    def test_test2_pjaxr_content_namespace(self):
        client = Client()
        response = client.get(reverse('content_1'), **{'HTTP_X_PJAX': 'true', 'HTTP_X_PJAX_NAMESPACE': 'Site1.Page1.Content2'})
        self.assertNotContains(response, self.page_1_string)
        self.assertContains(response, self.content_1_string)
        self.assertContains(response, '<pjaxr-body>')
        self.assertNotContains(response, '<html>')

    def test_test2_pjaxr_different_page_namespace(self):
        client = Client()
        response = client.get(reverse('content_1'), **{'HTTP_X_PJAX': 'true', 'HTTP_X_PJAX_NAMESPACE': 'Site1.Page2'})
        self.assertContains(response, self.page_1_string)
        self.assertContains(response, self.content_1_string)
        self.assertContains(response, '<pjaxr-body>')
        self.assertNotContains(response, '<html>')

    def test_test2_pjaxr_different_site_namespace(self):
        client = Client()
        response = client.get(reverse('content_1'), **{'HTTP_X_PJAX': 'true', 'HTTP_X_PJAX_NAMESPACE': 'Site2.Page1'})
        self.assertContains(response, self.page_1_string)
        self.assertContains(response, self.content_1_string)
        self.assertNotContains(response, '<pjaxr-body>')
        self.assertContains(response, '<html>')

    def test_test2_pjaxr_no_namespace(self):
        client = Client()
        response = client.get(reverse('content_1'), **{'HTTP_X_PJAX': 'true'})
        self.assertNotContains(response, self.page_1_string)
        self.assertContains(response, self.content_1_string)
        self.assertContains(response, '<pjaxr-body>')
        self.assertNotContains(response, '<html>')

    # testing with 2 different namespaces

    def test_test3_no_pjaxr(self):
        client = Client()
        response = client.get(reverse('content_2'))
        self.assertContains(response, self.content_2_string)
        self.assertContains(response, self.page_1_string)
        self.assertContains(response, '<html>')
        self.assertNotContains(response, '<pjaxr-body>')

    def test_test3_pjaxr_with_namespace(self):
        client = Client()
        response = client.get(reverse('content_2'), **{'HTTP_X_PJAX': 'true', 'HTTP_X_PJAX_NAMESPACE': 'Site1.Page1.Content1'})
        self.assertContains(response, self.content_2_string)
        self.assertNotContains(response, self.page_1_string)
        self.assertContains(response, '<pjaxr-body>')
        self.assertNotContains(response, '<html>')

    def test_test3_pjaxr_different_page_namespace(self):
        client = Client()
        response = client.get(reverse('content_2'), **{'HTTP_X_PJAX': 'true', 'HTTP_X_PJAX_NAMESPACE': 'Site1.Page2'})
        self.assertContains(response, self.content_2_string)
        self.assertContains(response, self.page_1_string)
        self.assertContains(response, '<pjaxr-body>')
        self.assertNotContains(response, '<html>')

    def test_test3_pjaxr_different_site_namespace(self):
        client = Client()
        response = client.get(reverse('content_2'), **{'HTTP_X_PJAX': 'true', 'HTTP_X_PJAX_NAMESPACE': 'Site2.Page1.Content1'})
        self.assertContains(response, self.content_2_string)
        self.assertContains(response, self.page_1_string)
        self.assertNotContains(response, '<pjaxr-body>')
        self.assertContains(response, '<html>')

    def test_test3_pjaxr_no_namespace(self):
        client = Client()
        response = client.get(reverse('content_2'), **{'HTTP_X_PJAX': 'true'})
        self.assertContains(response, self.content_2_string)
        self.assertNotContains(response, self.page_1_string)
        self.assertContains(response, '<pjaxr-body>')
        self.assertNotContains(response, '<html>')
