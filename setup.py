import sys

from setuptools import setup, find_packages

py_version = sys.version_info[:2]
PY2 = py_version[0] == 2

if PY2:
    if py_version < (2, 6):
        raise RuntimeError('Python 2.6 or higher is required.')
else:
    if py_version < (3, 3):
        raise RuntimeError('Python 3.3 or higher is required.')

with open('README') as fp:
    long_desc = fp.read()

setup(name="flatland",
      version='0.1dev',
      packages=find_packages(exclude=['tests.*', 'tests']),
      author='Jason Kirtland',
      author_email='jek@discorporate.us',
      description='HTML form management and validation',
      keywords='schema validation data web form forms roundtrip',
      long_description=long_desc,
      license='MIT License',
      url='http://discorporate.us/jek/projects/flatland/',
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.5',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Internet :: WWW/HTTP :: WSGI',
                   'Topic :: Software Development :: Libraries'],
      install_requires=[
          'blinker',
      ],
      tests_require=[
          'genshi',
          'sphinx',
          'nose',
      ],
      include_package_data=True,
      zip_safe=True,
      )
