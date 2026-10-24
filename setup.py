from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements_list = []
    with open(file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                if line != HYPEN_E_DOT:
                    requirements_list.append(line)
    return requirements_list

setup(
    name="my_project",
    version="0.1",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)