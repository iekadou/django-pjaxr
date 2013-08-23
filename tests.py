from __future__ import unicode_literals
from django.conf.urls import patterns
from django.test import TestCase, Client
from django.views.generic import TemplateView


class Test1View(TemplateView):
    template_name = 'tests/test1.html'


class Test2View(TemplateView):
    template_name = 'tests/test2.html'


class Test3View(TemplateView):
    template_name = 'tests/test3.html'


urlpatterns = patterns('',
    (r'^test1/$',   Test1View.as_view()),
    (r'^test2/$',   Test2View.as_view()),
    (r'^test3/$',   Test3View.as_view()),
)


class TestPjaxrRequests(TestCase):

    urls = 'django_pjaxr.tests'
    test1string = 'Testsite1'
    test2string = 'Testsite2'
    test3string = 'Testsite3'

    # testing with 1 namespace

    def test_test1_no_pjaxr(self):
        client = Client()
        response = client.get('/test1/')
        self.assertContains(response, self.test1string)
        self.assertNotContains(response, self.test2string)
        self.assertContains(response, '<html>')
        self.assertNotContains(response, '<pjaxr-body>')

    def test_test1_pjaxr_with_namespace(self):
        client = Client()
        response = client.get('/test1/', **{'HTTP_X_PJAX': 'true', 'HTTP_X_PJAX_NAMESPACE': 'Testsuite'})
        self.assertContains(response, self.test1string)
        self.assertNotContains(response, self.test2string)
        self.assertContains(response, '<pjaxr-body>')
        self.assertNotContains(response, '<html>')

    def test_test1_pjaxr_wrong_namespace(self):
        client = Client()
        response = client.get('/test1/', **{'HTTP_X_PJAX': 'true', 'HTTP_X_PJAX_NAMESPACE': 'wrong'})
        self.assertContains(response, self.test1string)
        self.assertNotContains(response, self.test2string)
        self.assertNotContains(response, '<pjaxr-body>')
        self.assertContains(response, '<html>')

    def test_test1_pjaxr_no_namespace(self):
        client = Client()
        response = client.get('/test1/', **{'HTTP_X_PJAX': 'true'})
        self.assertContains(response, self.test1string)
        self.assertNotContains(response, self.test2string)
        self.assertContains(response, '<pjaxr-body>')
        self.assertNotContains(response, '<html>')

    # testing with 2 hierarchically structured namespaces

    def test_test2_no_pjaxr(self):
        client = Client()
        response = client.get('/test2/')
        self.assertContains(response, self.test1string)
        self.assertContains(response, self.test2string)
        self.assertContains(response, '<html>')
        self.assertNotContains(response, '<pjaxr-body>')

    def test_test2_pjaxr_parent_namespace(self):
        client = Client()
        response = client.get('/test2/', **{'HTTP_X_PJAX': 'true', 'HTTP_X_PJAX_NAMESPACE': 'Testsuite'})
        self.assertContains(response, self.test1string)
        self.assertContains(response, self.test2string)
        self.assertContains(response, '<pjaxr-body>')
        self.assertNotContains(response, '<html>')

    def test_test2_pjaxr_current_namespace(self):
        client = Client()
        response = client.get('/test2/', **{'HTTP_X_PJAX': 'true', 'HTTP_X_PJAX_NAMESPACE': 'Testsuite.Detail'})
        self.assertNotContains(response, self.test1string)
        self.assertContains(response, self.test2string)
        self.assertContains(response, '<pjaxr-body>')
        self.assertNotContains(response, '<html>')

    def test_test2_pjaxr_wrong_namespace(self):
        client = Client()
        response = client.get('/test2/', **{'HTTP_X_PJAX': 'true', 'HTTP_X_PJAX_NAMESPACE': 'wrong'})
        self.assertContains(response, self.test1string)
        self.assertContains(response, self.test2string)
        self.assertNotContains(response, '<pjaxr-body>')
        self.assertContains(response, '<html>')

    def test_test2_pjaxr_no_namespace(self):
        client = Client()
        response = client.get('/test2/', **{'HTTP_X_PJAX': 'true'})
        self.assertNotContains(response, self.test1string)
        self.assertContains(response, self.test2string)
        self.assertContains(response, '<pjaxr-body>')
        self.assertNotContains(response, '<html>')

    # testing with 2 different namespaces

    def test_test3_no_pjaxr(self):
        client = Client()
        response = client.get('/test3/')
        self.assertContains(response, self.test3string)
        self.assertNotContains(response, self.test1string)
        self.assertContains(response, '<html>')
        self.assertNotContains(response, '<pjaxr-body>')

    def test_test3_pjaxr_with_namespace(self):
        client = Client()
        response = client.get('/test3/', **{'HTTP_X_PJAX': 'true', 'HTTP_X_PJAX_NAMESPACE': 'NewSuite'})
        self.assertContains(response, self.test3string)
        self.assertNotContains(response, self.test1string)
        self.assertContains(response, '<pjaxr-body>')
        self.assertNotContains(response, '<html>')

    def test_test3_pjaxr_wrong_namespace(self):
        client = Client()
        response = client.get('/test3/', **{'HTTP_X_PJAX': 'true', 'HTTP_X_PJAX_NAMESPACE': 'wrong'})
        self.assertContains(response, self.test3string)
        self.assertNotContains(response, self.test1string)
        self.assertNotContains(response, '<pjaxr-body>')
        self.assertContains(response, '<html>')

    def test_test3_pjaxr_different_namespace(self):
        client = Client()
        response = client.get('/test3/', **{'HTTP_X_PJAX': 'true', 'HTTP_X_PJAX_NAMESPACE': 'Testsuite'})
        self.assertContains(response, self.test3string)
        self.assertNotContains(response, self.test1string)
        self.assertNotContains(response, '<pjaxr-body>')
        self.assertContains(response, '<html>')

    def test_test3_pjaxr_no_namespace(self):
        client = Client()
        response = client.get('/test3/', **{'HTTP_X_PJAX': 'true'})
        self.assertContains(response, self.test3string)
        self.assertNotContains(response, self.test1string)
        self.assertContains(response, '<pjaxr-body>')
        self.assertNotContains(response, '<html>')