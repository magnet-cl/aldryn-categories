
from setuptools import setup, find_packages
from aldryn_categories import __version__

# git tag '[version]'
# git push --tags origin master
# python setup.py sdist upload
# python setup.py bdist_wheel upload

setup(
    name='aldryn-categories',
    version=__version__,
    url='https://github.com/aldryn/aldryn-categories',
    license='BSD License',
    description='Hierarchical categories/taxonomies for your Django project',
    author='Divio AG',
    author_email='info@divio.ch',
    package_data={},
    packages=find_packages(),
    platforms=['OS Independent'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 5.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
    ],
    python_requires='>=3.8',
    install_requires=[
        'django>=3.2,<6.0',
        'django-parler',
        'django-treebeard',
        'aldryn-translation-tools @ git+https://github.com/magnet-cl/aldryn-translation-tools.git#0.3.1-post2',
    ],
    include_package_data=True,
    zip_safe=False
)
