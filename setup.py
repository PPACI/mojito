from setuptools import setup, find_packages

with open("Readme.md") as f:
    long_desc = f.read()

setup(
        name='mojito-mock',
        version='0.3.0',
        packages=find_packages(),
        license='',
        author='Pierre Paci',
        author_email='',
        description='Mocking temporal data made easy !',
        long_description=long_desc,
        url="https://github.com/PPACI/mojito",
        long_description_content_type="text/markdown",
        classifiers=(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: Apache Software License",
            "Topic :: Scientific/Engineering :: Mathematics",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Scientific/Engineering"
        ),
        install_requires=[
            "numpy==1.13.3",
            "scipy==1.1.0"
            ]
        )
