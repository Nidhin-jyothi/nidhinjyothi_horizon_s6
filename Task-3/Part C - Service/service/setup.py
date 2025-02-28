from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'service'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nidhin',
    maintainer_email='nidhin@todo.todo',
    description='Calculator service package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'calc_server = service.calc_server:main',
            'calc_client = service.calc_client:main',
        ],
    },
)