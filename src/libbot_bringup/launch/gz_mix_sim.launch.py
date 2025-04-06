import os
import xacro

from launch import LaunchDescription
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    package_name = 'libbot_bringup'
    package_share = FindPackageShare(package=package_name).find(package_name)

    use_uros_agent = LaunchConfiguration('use_uros_agent')
    uros_serial_port = LaunchConfiguration('uros_serial_port')
    uros_serial_baudrate = LaunchConfiguration('uros_serial_baudrate')

    declare_use_uros_agent = DeclareLaunchArgument(
        name='use_uros_agent',
        default_value='true',
        description='Whether to launch micro ros agent'
    )

    declare_uros_serial_port = DeclareLaunchArgument(
        name='uros_serial_port', 
        default_value='/dev/ttyACM0',
        description='The serial communication port for micro ros'
    )

    declare_uros_serial_baudrate = DeclareLaunchArgument(
        name='uros_serial_baudrate', 
        default_value='115200',
        description='The serial communication baud rate for micro ros'
    )

    micro_ros_agent = Node(
        condition=IfCondition(use_uros_agent),
        package='micro_ros_agent',
        executable='micro_ros_agent',
        output='screen',
        arguments=['serial', '--dev', uros_serial_port, '--baudrate', uros_serial_baudrate]
    )

    package_libbot_gazebo = FindPackageShare(package='libbot_gazebo').find('libbot_gazebo')
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(package_libbot_gazebo, 'launch', 'gazebo.launch.py')),
            launch_arguments={
                'use_rviz': 'false',
        }.items()
    )

    ld = LaunchDescription()
    
    ld.add_action(declare_use_uros_agent)
    ld.add_action(declare_uros_serial_port)
    ld.add_action(declare_uros_serial_baudrate)

    ld.add_action(micro_ros_agent)
    ld.add_action(gazebo)
    

    return ld