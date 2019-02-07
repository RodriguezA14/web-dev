try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Marcus',
    'url': 'https://ide.c9.io/marcusaj0114/web-dev',
    'download_url': 'https://ide.c9.io/marcusaj0114/web-dev',
    'author_email': 'student.150918@worcesterschools.net',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'myenv'
}

setup(**config)