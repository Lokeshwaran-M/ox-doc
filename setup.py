import os
from setuptools import setup, find_packages

setup(
    name="ox-doc",
    version="0.0.71",
    description="A lib to handle documents read write of different data structures efficiently and serialization, deserialization and processing",
    author="Lokeshwaran M",
    author_email="lokeshwaran.m23072003@gmail.com",
    url="https://github.com/ox-ai/ox-doc.git",
    license="MIT",
    packages=find_packages(),
    package_data={"": ["requirements.txt", "README.md"]},
    install_requires=open("requirements.txt").readlines(),
    keywords="ox-doc ox-ai",
)
