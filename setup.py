from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'IndicatorAPI.com wrapper'
LONG_DESCRIPTION = 'A package that allows developers to use indicatorapi quickly.'
project_urls = {'GitHub': 'https://github.com/dreistein33/pyIndicatorAPI'}
# Setting up
setup(
    name="pyIndicatorAPI",
    version=VERSION,
    author="dreistein33",
    author_email="kjuchnowski@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    project_urls=project_urls,
    install_requires=['datetime', 'requests'],
    keywords=['python', 'indicatorapi', 'api', 'crypto'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)