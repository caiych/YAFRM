from setuptools import setup, find_packages
setup(
        name="YAFRM",
        version="0.0.1",
        description="Yet Another Flask-Restful Module",
        keywords="flask restful",
        author="Caiych",
        author_email='me@caiych.cc',
        url="https://github.com/caiych/YAFRM",
        license="LGPL",
        packages= find_packages(),
        install_requires=[
            'Flask>=0.8', 
            ]
        )
