#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="brainlift-cli",
    version="0.1.0",
    description="BrainLift CLI - A command-line interface for the BrainLift knowledge management system",
    author="Trilogy Group",
    author_email="info@trilogy.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.25.0",
        "python-dotenv>=0.15.0",
    ],
    entry_points={
        "console_scripts": [
            "blm=blm:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
