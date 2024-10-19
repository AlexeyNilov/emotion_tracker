from setuptools import find_packages
from setuptools import setup

VERSION = "0.0.12"
DESCRIPTION = "Feelings DB"

# Setting up
setup(
    name="feelings",
    version=VERSION,
    description=DESCRIPTION,
    include_package_data=True,
    packages=find_packages(exclude=["conf", "sample", "test"]),
    install_requires=["pyyaml"],
    python_requires=">=3.9",
)
