import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="common",
    version="1.0.0",
    author="SharkNinja_SQA",
    description="Common libraries including utilities for general use for all automation projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "requests",
        "python-dateutil",
        "tenacity",
        "paho-mqtt",
        "pyee",
        "protobuf==3.20.0",
        "pillow",
    ],
    python_requires=">=3.6",
)
