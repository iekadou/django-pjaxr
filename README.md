# django-pjaxr [![Build Status](https://secure.travis-ci.org/iekadou/django-pjaxr.png)](http://travis-ci.org/iekadou/django-pjaxr)

## How to install django-pjaxr?

There are just two steps needed to install django-pjaxr:

1. Install django-pjaxr to your virtual env:

	```bash
	pip install django-pjaxr
	```

2. Configure your django installation with the following lines:

	```python
	from django.template import add_to_builtins
	add_to_builtins('django_pjaxr.templatetags.pjaxr_extends')
	
	INSTALLED_APPS += ('django_pjaxr', )
	
	TEMPLATE_CONTEXT_PROCESSORS += ('django_pjaxr.context_processors.pjaxr_information',)
	
	DEFAULT_PJAXR_TEMPLATE = "django_pjaxr/pjaxr.html"
	```

## What do you need for django-pjaxr?

1. Django >= 1.3
2. [jquery-pjaxr](https://github.com/minddust/jquery-pjaxr)

Happy speeding up your django project!
