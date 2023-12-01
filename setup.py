from setuptools import find_packages,setup
from typing import List

HY_E='-e .'
def get_requirements(file_path:str)-> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]
        if HY_E in requirements:
            requirements.remove(HY_E)
    return requirements

setup(
name='ML_PROJECT',
version='0.0.1',
author='Sarath',
packages=find_packages(),
install= get_requirements('requirements.txt')

)