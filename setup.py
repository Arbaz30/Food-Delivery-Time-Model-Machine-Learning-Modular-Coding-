from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "Food Delivery Time Model Machine Learning Modular Coding"
VERSION = "0.0.1"
DESCRIPTION = "This is our machine learning project in modular encoding"
AUTHOR_NAME = "Arbaz Ali"
AUTHOR_EMAIL = "princearbaz23001@gmail.com"

REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

# requirements.txt file open
# read
# \n ""
def get_requirements_list()->list[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list



setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires = get_requirements_list()
)