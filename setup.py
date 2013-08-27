#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import re
import os
import sys


def get_version(package):
  """
  Return package version as listed in `__version__` in `init.py`.
  """
  init_py = open(os.path.join(package, '__init__.py')).read()
  return re.match("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_packages(package):
  """
  Return root package and all sub-packages.
  """
  return [dirpath
          for dirpath, dirnames, filenames in os.walk(package)
          if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
  """
  Return all files under the root package, that are not in a
  package themselves.
  """
  walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
          for dirpath, dirnames, filenames in os.walk(package)
          if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

  filepaths = []
  for base, filenames in walk:
      filepaths.extend([os.path.join(base, filename)
                        for filename in filenames])
  return {package: filepaths}


version = get_version('django_pjaxr')


if sys.argv[-1] == 'publish':
  os.system("python setup.py sdist upload")
  print("You probably want to also tag the version now:")
  print("  git tag -a %s -m 'version %s'" % (version, version))
  print("  git push --tags")
  sys.exit()


setup(name='django-pjaxr',
      version=version,
	  author='Jonas Braun',
	  author_email='jbraun@uni-koblenz.de',
      license='MIT',
	  url='http://noxic-action.de',
      description='Django extension to use jquery-pjaxr easily!',
      packages=get_packages('django_pjaxr'),
      package_data=get_package_data('django_pjaxr'),
      py_modules=['django-pjaxr'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Internet :: WWW/HTTP',
      ]
      )
      

# (*) Please direct queries to the discussion group, rather than to me directly
#     Doing so helps ensure your question is helpful to other users.
#     Queries directly to my email are likely to receive a canned response.
#
#     Many thanks for your understanding.