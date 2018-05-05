"""
setup for datasoreX
"""
from setuptools import setup

setup(name='datastorex',
      version='0.1',
      description='Provide abstraction for data manipulation over multiple data stores',
      url='https://github.com/kanekargauri/datastoreX.git',
      author='gauri kanekar',
      author_email='meetgaurikanekar@gmail.com',
      license='MIT',
      packages=['datastorex'],
      install_requires=['MySQL-python==1.2.5', 'pytest==2.9.1'],
      zip_safe=False)
