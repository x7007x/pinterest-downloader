from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pinterest_downloader",
    version="0.1.0",
    author="Ahmed Negm",
    author_email="a7mednegm.x@gmail.com",
    description="A Pinterest media downloader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/x7007x/pinterest-downloader",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)