from setuptools import setup, find_packages


setup(
    name='django-ajax',
    version='1.0.0rc1',
    description='A simple framework for creating AJAX endpoints in Django.',
    long_description='',
    keywords='django, ajax',
    author='Amplify Nation',
    author_email='tech@amplify-nation.com',
    url='https://github.com/amplify-nation/django-ajax',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['decorator',],
    extras_require = {
        'Tagging': ['taggit']
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ]
)
