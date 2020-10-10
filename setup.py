import os

from setuptools import setup, find_namespace_packages

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    requirements = ''
    for line in f.readlines():
        if not line.startswith('-i'):
            requirements += line

setup(
    name='wise_elders_user',
    description='',
    packages=find_namespace_packages(include=['wise_elders.*']),
    install_requires=requirements,
)
