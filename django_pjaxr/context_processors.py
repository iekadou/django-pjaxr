def pjaxr_information(request):
    """
    passes the pjax head information to the templates
    """

    response = {
        'pjaxr': request.META.get('HTTP_X_PJAX', False),
    }

    if request.META.get('HTTP_X_PJAX_NAMESPACE', False):
        response.update({
            'pjaxr_namespace': request.META['HTTP_X_PJAX_NAMESPACE'],
        })

    return response
