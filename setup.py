from setuptools import find_packages, setup
from typing import List


def install_requirements(file_path:str)->List[str]:
    """
    It is for installing the all packages
    """
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [ele.replace('\n','') for ele in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    
    return requirements


setup(
    name='Gulshan',
    version='0.0.2',
    packages=find_packages(),
    install_req = install_requirements('requirements.txt')
)