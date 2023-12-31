from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "1.0.0"
DESCRIPTION = "Telebirr integration"
LONG_DESCRIPTION = "This package is a helper package with telebirr integration."

# Setting up
setup(
    name="Telebirr",
    version=VERSION,
    license="MIT",
    author="MrProfessional Hacker",
    author_email="<MrProfessionalHacker@outlook.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["pycryptodome", "requests", "cryptography"],
    keywords=["python", "telebirr", "payment", "ethiopia", "ethio telecom"],
    url="https://telebirrapp.github.io/TelebirrApp/",
    download_url="https://github.com/TelebirrApp/TelebirrApp/releases/tag/V1.0.0",
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
