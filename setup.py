import io
import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with io.open('sheetfu/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)


setup(
    name='sheetfu',
    packages=['sheetfu'],
    description='Sheetfu is a library to interact with Google sheets.',
    long_description='Sheetfu long description coming soon ...',
    version=version,
    author='Philippe Oger',
    author_email='phil.oger@gmail.com',
    url='https://github.com/socialpoint-labs/sheetfu',
    keywords=['spreadsheets', 'google-spreadsheets'],
    install_requires=['google-api-python-client>=1.7.4', 'oauth2client>=4.1.2'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Software Development :: Libraries :: Python Modules"
        ],
    license='MIT'
)
