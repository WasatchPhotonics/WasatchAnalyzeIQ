try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": " Acquire data from Wasatch Photonics spectrometers for use in AnalyzeIQ",
    "author": "Nathan Harrington",
    "url": "https://github.com/nharringtonwasatch/WasatchAnalyzeIQ",
    "download_url": "https://github.com/nharringtonwasatch/WasatchAnalyzeIQ",
    "author_email": "nharrington@wasatchphotonics.com.",
    "version": "1.0.0",
    "install_requires": ["numpy"],
    "packages": ["WasatchAnalyzeIQ"],
    "scripts": [],
    "name": "WasatchAnalyzeIQ"
}

setup(**config)
