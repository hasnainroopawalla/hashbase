from setuptools import setup, find_packages
import os

repository_dir = os.path.dirname(__file__)

with open(os.path.join(repository_dir, "README.md")) as fh:
    long_description = fh.read()

setup(
    name="hashbase",
    version="1.0.6",
    packages=find_packages(exclude="tests"),
    description="A collection of cryptographic hashing algorithms implemented in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hasnainroopawalla/hashbase",
    author="Hasnain Roopawalla",
    author_email="hasnain.roopawalla@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="python, hashing, hashing-algorithms, hash-functions, cryptography",
    python_requires=">=3.6",
)
