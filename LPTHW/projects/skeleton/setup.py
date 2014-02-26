try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
        'description':'My Project',
        'author':'David G Shields',
        'url':'https://github.com/salacio',
        'download_url':'Where to download it.',
        'author_email':'salacio@gmail.com',
        'version':'0.1',
        'install_requires':['nose'],
        'packages':['NAME'],
        'scripts':[],
        'name':'projectname'
        }

setup(**config)
