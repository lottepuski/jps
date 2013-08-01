try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Movie Browser',
    'author': 'Nagaravind Challakere',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['moviebrowser'],
    'scripts': [],
    'name': 'moviebrowser'
}

setup(**config)
