from django.views.generic import TemplateView
from django_pjaxr.mixins import PjaxrMixin


class Page1View(PjaxrMixin, TemplateView):
    template_name = 'tests/page_1.html'
    namespace = "Site1.Page1"

    def get_context_data(self, **kwargs):
        result = super(Page1View, self).get_context_data(**kwargs)
        if self.pjaxr_site:
            result.update({'site_string': 'site_1'})
        if self.pjaxr_page:
            result.update({'page_string': 'page_1'})
        return result


class Page1Content1View(PjaxrMixin, TemplateView):
    template_name = 'tests/page_1_content_1.html'
    namespace = "Site1.Page1.Content1"

    def get_context_data(self, **kwargs):
        result = super(Page1Content1View, self).get_context_data(**kwargs)
        if self.pjaxr_site:
            result.update({'site_string': 'site_1'})
        if self.pjaxr_page:
            result.update({'page_string': 'page_1'})
        if self.pjaxr_content:
            result.update({'content_string': 'content_1'})
        return result


class Page1Content1InnerContent1View(PjaxrMixin, TemplateView):
    template_name = 'tests/page_1_content_1_inner_content_1.html'
    namespace = "Site1.Page1.Content1.InnerContent1"

    def get_context_data(self, **kwargs):
        result = super(Page1Content1InnerContent1View, self).get_context_data(**kwargs)
        if self.pjaxr_site:
            result.update({'site_string': 'site_1'})
        if self.pjaxr_page:
            result.update({'page_string': 'page_1'})
        if self.pjaxr_content:
            result.update({'content_string': 'content_1'})
        if self.pjaxr_inner_content:
            result.update({'inner_content_string': 'inner_con_tent_1'})
        return result


class Page1Content1InnerContent2View(PjaxrMixin, TemplateView):
    template_name = 'tests/page_1_content_1_inner_content_2.html'
    namespace = "Site1.Page1.Content1.InnerContent2"

    def get_context_data(self, **kwargs):
        result = super(Page1Content1InnerContent2View, self).get_context_data(**kwargs)
        if self.pjaxr_site:
            result.update({'site_string': 'site_1'})
        if self.pjaxr_page:
            result.update({'page_string': 'page_1'})
        if self.pjaxr_content:
            result.update({'content_string': 'content_1'})
        if self.pjaxr_content:
            result.update({'inner_content_string': 'inner_con_tent_2'})
        return result


class Page1Content2View(PjaxrMixin, TemplateView):
    template_name = 'tests/page_1_content_2.html'
    namespace = "Site1.Page1.Content2"

    def get_context_data(self, **kwargs):
        result = super(Page1Content2View, self).get_context_data(**kwargs)
        if self.pjaxr_site:
            result.update({'site_string': 'site_1'})
        if self.pjaxr_page:
            result.update({'page_string': 'page_1'})
        if self.pjaxr_content:
            result.update({'content_string': 'content_2'})
        return result


class Page2View(PjaxrMixin, TemplateView):
    template_name = 'tests/page_2.html'
    namespace = "Site1.Page2"

    def get_context_data(self, **kwargs):
        result = super(Page2View, self).get_context_data(**kwargs)
        if self.pjaxr_site:
            result.update({'site_string': 'site_1'})
        if self.pjaxr_page:
            result.update({'page_string': 'page_2'})
        return result
