from setuptools import setup, find_packages

setup(
    name='django-crumbs',
    version=__import__('crumbs').__version__,
    author='Caktus Consulting Group',
    author_email='solutions@caktusgroup.com',
    include_package_data=True,
    packages=['crumbs', 'crumbs.templatetags', 'crumbs.tests'],
    package_dir={'crumbs':'crumbs'},
    package_data={'': ['README.rst'], 'crumbs': ['crumbs/templates/*.*']},
    exclude_package_data={'': ['.gitignore']},
    url='http://github.com/artscoop/django-crumbs/',
    license='BSD',
    description='A pluggable Django app for adding breadcrumbs to your project. ',
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=open('README.rst').read(),
    test_suite="runtests.runtests",
    zip_safe=False,
)

