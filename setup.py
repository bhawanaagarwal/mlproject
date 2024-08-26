from setuptools import find_packages, setup
from typing import List

HYPHEN_e = '-e .'

def get_requirements(file_path:str)-> List[str]:
    '''
    This function will return the list of pacakges required for this file.

    Input: File path of the requirements.txt

    '''


    requirements=[]

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
    
    if HYPHEN_e in requirements:
        requirements.remove(HYPHEN_e)

    return requirements


setup(

    name = 'mlproject',
    version = '0.0.1',
    author = 'Bhawana',
    author_email= 'agarwalbhawana92@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)