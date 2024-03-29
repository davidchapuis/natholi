#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests',
    'pandas',
    'json',
]

test_requirements = ['pytest>=3', ]

setup(
    author="David Chapuis",
    author_email='dah.chapuis@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A package allowing you to get national holidays for 200+ countries around the world in one line of code.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='natholi',
    name='natholi',
    packages=find_packages(include=['natholi', 'natholi.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/davidchapuis/natholi',
    version='0.1.1',
    zip_safe=False,
)
