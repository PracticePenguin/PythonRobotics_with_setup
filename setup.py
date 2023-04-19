from setuptools import setup
from setuptools import find_namespace_packages

setup(name='PythonRobotics',
      version='1.0',
      description='PythonRobotics modules',
      author='Atsushi Sakai',
      url='https://github.com/AtsushiSakai/PythonRobotics.git',
      packages=find_namespace_packages(include=["PathPlanning", "PathPlanning.*"]),
      install_requires=[
            "numpy == 1.24.2",
            "scipy == 1.10.1",
            "matplotlib == 3.7.1",
            "cvxpy == 1.3.1",
            "pytest == 7.3.0",
            "pytest-xdist == 3.2.1",
            "mypy == 1.2.0",
            "ruff == 0.0.261"],
     )
