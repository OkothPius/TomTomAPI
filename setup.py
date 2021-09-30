import os

from setuptools import find_packages, setup

VERSION = __import__("import_export").__version__

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Software Development',
]

install_requires = [
    'diff-match-patch',
    'Django>=2.0',
    'tablib[html,ods,xls,xlsx,yaml]>=0.14.0',
]


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    readme = f.read()


setup(
    name="TomTom API",
    description="Visualization of TomTom traffic and routing API",
    long_description=readme,
    version=VERSION,
    author="Oruko Pius",
    author_email="orukopius8@gmail.com",
    license='MIT License',
    platforms=['OS Independent'],
    url="https://github.com/django-import-export/django-import-export",
    project_urls={
        "Documentation": "https://django-import-export.readthedocs.io/en/stable/",
        "Changelog": "https://django-import-export.readthedocs.io/en/stable/changelog.html",
    },
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=install_requires,
    python_requires=">=3.6",
    classifiers=CLASSIFIERS,
    zip_safe=False,
)

