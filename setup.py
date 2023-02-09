"""
Setup file for the cultureai package.

This file is used to install the package with pip.
"""
from pathlib import Path

from setuptools import find_packages, setup

ROOT = Path(__file__).parent.absolute()

setup(
    name="leetcode-problems",
    version="0.0.1",
    package_dir={"": "src"},
    packages=find_packages(exclude=["tests", "tests.*"]),
    description="Collection of leetcode problems",
    long_description_content_type="text/markdown",
)
