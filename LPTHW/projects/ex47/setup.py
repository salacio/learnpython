try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
        'description':'ex47',
        'author':'David G Shields',
        'url':'https://github.com/salacio',
        'download_url':'https://github.com/salacio/learnpython/LPTHW/projects/ex47',
        'author_email':'salacio@gmail.com',
        'version':'0.1',
        'install_requires':['nose'],
        'packages':['ex47'],
        'scripts':[],
        'name':'ex47'
        }

setup(**config)
