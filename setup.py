from setuptools import setup

setup(
        name='mojito',
        version='0.2.0',
        packages=['mojito'],
        url='smart-metric.com',
        license='',
        author='Pierre Paci',
        author_email='',
        description='Mocking temporal data made easy !',
        install_requires=[
            "numpy==1.13.3",
            "scipy==1.1.0"
            ]
        )
