from distutils.core import setup

from setuptools import find_packages

setup(
    name='bonk-cli',
    version='0.0.1',
    description='Util to bonk vatniks',
    author='Alberto Calderari',
    author_email='',
    url='https://github.com/albertocalderari/bonk-cli',
    packages=find_packages(exclude='./tests'),
    entry_points={
        'console_scripts': [
            'bonkcli=bonkcli.cli:main',
        ],
    },
    install_requires=[
        "tweepy==4.10.1",
        "algebraic-data-types==0.2.1",
        "pydantic==1.10.2",
        "inquirer==3.0.0"
    ]
)
