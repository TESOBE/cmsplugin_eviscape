from setuptools import setup, find_packages

version = __import__('cmsplugin_eviscape').__version__

setup(
    name = "cmsplugin_eviscape",
    version = version,
    url = 'https://github.com/TESOBE/cmsplugin_eviscape',
    license = 'BSD',
    platforms=['OS Independent'],
    description = "An Eviscape extension for Django CMS",
    author = "Tim Kleinschmidt, Tobias Pfeiffer",
    author_email = 'tim@tesobe.com, tobias@tesobe.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    package_dir={
        'cmsplugin_eviscape': 'cmsplugin_eviscape',
    },
    install_requires = [
            "Django >= 1.3",
            "django-cms >= 2.2",
    ]
)