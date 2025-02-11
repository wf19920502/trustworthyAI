# -*- coding:utf-8 -*-
"""Setuptools of castle."""
import setuptools
import sys


if sys.version_info < (3, 6):
    sys.exit("Sorry, Python < 3.6 is not supported.")


with open("README.md", "r") as fh:
    long_desc = fh.read()


setuptools.setup(
    name="gcastle",
    version="1.0.0",
    # packages=["gcastle"],
    include_package_data=True,
    python_requires=">=3.6",
    author="Huawei Noah's Ark Lab",
    author_email="zhangkeli1@huawei.com",
    description="Pipeline for causal structure learning",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://gitlab.huawei.com/gtsbrain/project/causal_discovery/pcastle",
    packages=setuptools.find_packages(),
    license="Apache license",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "tqdm>=4.48.2",
        "numpy>=1.19.1",
        "pandas>=0.22.0",
        "scipy>=1.4.1",
        "scikit-learn>=0.21.1",
        "matplotlib>=2.1.2",
        "python-igraph>=0.8.2",
        "loguru>=0.5.3",
        "networkx>=2.5",
        "torch>=1.4.0",
        "tensorflow==1.15.0",
    ],
)

