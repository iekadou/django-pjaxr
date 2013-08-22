# Django-pjaxr

## How to install Django-pjaxr?

There are just two steps needed to install django-pjaxr:

1. Install django-pjaxr to your virtual env:

```bash
pip install django-pjaxr
```
	

2. Configure your django installation with the following lines:

```python
from django.template import add_to_builtins
add_to_builtins('django_pjaxr.templatetags.pjaxr_extends')

TEMPLATE_CONTEXT_PROCESSORS += ('django_pjaxr.context_processors.pjaxr_information',)

INSTALLED_APPS += ('django_pjaxr', )

DEFAULT_PJAXR_TEMPLATE = "django_pjaxr/pjaxr.html"
```
