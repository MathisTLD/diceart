from setuptools import setup, find_packages  # type: ignore

setup(
    name="testutils",
    version="0.0",
    packages=find_packages(include=("testutils*",)),
    install_requires=[],
)
