import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'libbot_lib_interface'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='devesh',
    maintainer_email='devesh.k1203@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'library_server = libbot_lib_interface.library_server:main',
            'door_trajectory_publisher = libbot_lib_interface.door_trajectory_publisher:main',
        ],
    },
)
