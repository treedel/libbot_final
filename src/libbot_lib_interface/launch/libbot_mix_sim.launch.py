from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument, AppendEnvironmentVariable, IncludeLaunchDescription

import os
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    package_name = 'libbot_lib_interface'
    package_share = FindPackageShare(package=package_name).find(package_name)

    package_libbot_gazebo = FindPackageShare(package='libbot_gazebo').find('libbot_gazebo')
    gazebo_preconfigured = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(package_libbot_gazebo, 'launch', 'gazebo.launch.py')),
            launch_arguments={
                'use_rviz': 'false',
                'use_ekf_odom': 'true',
                'use_sim_time': 'true',
        }.items()
    )

    package_libbot_arduino = FindPackageShare(package='libbot_arduino').find('libbot_arduino')
    hardware_preconfigured = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(package_libbot_arduino, 'launch', 'libbot_hw.launch.py')),
            launch_arguments={
                'use_rviz': 'false',
                'use_mixed_simulation': 'true',
        }.items()
    )

    door_trajectory_publisher = Node(
        package="libbot_lib_interface",
        executable="door_trajectory_publisher",
        output='screen',
    )

    ld = LaunchDescription()

    ld.add_action(gazebo_preconfigured)
    ld.add_action(hardware_preconfigured)
    ld.add_action(door_trajectory_publisher)

    return ld