from setuptools import setup
from setuptools import find_namespace_packages

setup(name='PythonRobotics',
      version='1.0',
      description='PythonRobotics modules',
      author='Atsushi Sakai',
      url='https://github.com/AtsushiSakai/PythonRobotics.git',
      packages=find_namespace_packages(where=['PathPlanning']),
     )
