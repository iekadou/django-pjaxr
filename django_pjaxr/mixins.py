class PjaxrMixin(object):
    """
    View mixin that provides pjaxr functionality
    """
    namespace = ""
    parent_namespace = ""
    matching_count = 0

    def get_matching_count(self, request):
        """
        takes current_namespace to return the matching namespaces of the previous pjaxr-request and the current
        """
        if not self.is_pjaxr_request(request):
            return 0
        current_namespaces = self.namespace.split(".")
        previous_namespaces = self.get_previous_namespace(request).split(".")
        level = 0
        matching_count = 0
        while level < len(previous_namespaces) and level < len(current_namespaces):
            if previous_namespaces[level] == current_namespaces[level]:
                level += 1
                matching_count = level
            else:
                break
        return matching_count

    def get_previous_namespace(self, request):
        if self.is_pjaxr_request(request) and request.META.get('HTTP_X_PJAX_NAMESPACE', False):
            return request.META['HTTP_X_PJAX_NAMESPACE']
        return ""

    def is_pjaxr_request(self, request):
        return True if request.META.get('HTTP_X_PJAX_NAMESPACE', False) else False

    def get_context_data(self, **kwargs):
        context = super(PjaxrMixin, self).get_context_data(**kwargs)
        context.update({'pjaxr_namespace_current': self.namespace})
        context.update({'pjaxr_namespace_parent': self.parent_namespace})
        return context


class IekadouPjaxrMixin(PjaxrMixin):
    pjaxr_site = True
    pjaxr_page = True
    pjaxr_content = True
    pjaxr_inner_content = True

    def dispatch(self, request, *args, **kwargs):
        self.matching_count = self.get_matching_count(request)
        self.pjaxr_site = self.matching_count <= 0
        self.pjaxr_page = self.matching_count <= 1
        self.pjaxr_content = self.matching_count <= 2
        self.pjaxr_inner_content = self.matching_count <= 3
        return super(IekadouPjaxrMixin, self).dispatch(request, *args, **kwargs)
