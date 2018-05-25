from setuptools import setup

setup(
        name='mojito',
        version='0.1',
        packages=['mojito'],
        url='smart-metric.com',
        license='',
        author='Pierre Paci',
        author_email='',
        description='Mocking temporal data made easy !',
        install_requires=[
            "pandas==0.22.0",
            "numpy==1.13.3",
            "scipy==1.1.0"
            ]
        )
