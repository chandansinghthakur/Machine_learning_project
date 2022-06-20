from setuptools import setup
from typing import List



# Declearing the variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="CHANDAN"
DESCRIPTION="This is my first project"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """Descripton: This function reads the requirements file and returns a list of requirements"""
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
name =PROJECT_NAME,
version =VERSION,
author =AUTHOR,
description =DESCRIPTION,
packages =PACKAGES,
install_requires =get_requirements_list()
)

