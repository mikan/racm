"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['src/racm.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True,
           'site_packages': True,
           'iconfile': 'resources/icons/racm.icns'}

setup(
    app=APP,
    name='RACM',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
