from setuptools import setup
import os.path
__dir__ = os.path.dirname(os.path.abspath(__file__))

setup(
    name='Crowd',
    license='GPL v3',
    py_modules=['crowd'],
    version='0.6',
    install_requires=['requests'],

    description='A python client to the Atlassian Crowd REST API',
    long_description=open(os.path.join(__dir__, 'README.rst')).read(),

    author='Alexander Else',
    author_email='aelse@else.id.au',
    url='https://github.com/aelse/python-crowd',

    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration :: Authentication/Directory",
    ]
)
