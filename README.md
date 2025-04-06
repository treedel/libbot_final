# libbot_uros

## Installation instructions
- Install the required dependencies using rosdep
  > rosdep install --from-paths src --ignore-src -r -y

- Install nav2-bringup using the following command
  > sudo apt install ros-<ros2-distro>-nav2-bringup

- Create a micro ROS agent by following the steps present in the following link
  - https://micro.ros.org/docs/tutorials/core/first_application_linux/

A logistics system that assists in libraries using ROS2 and Nav2 for autonomous navigation.

## Current progress:
- Configured workspace
- Created URDF and 3D model of robot
- Integrated controllers for door arm joints and movement in Gazebo sim
- Implemented SLAM and NAV2 for autonomous navigation
- Prepared custom world for simulation
- Created server node to manage database and connect with ros
- Created CLI Interface for users to utilize the system
- Created CLI Interface for staffs to maintain the system
- Prepared interface code to attach ros and hardware using microROS
- Assembled the robot and tested all the functionalities
  
## Todo:
- [x] Make the repo cleaner by separating it into different packages
- [x] Design a library control flow
- [x] Prepare library control database and management system
- [x] Design application for managing system
- [x] Develop packages for integrating these with ROS system
- [x] Design hardware implementation flow
- [x] Find and source missing hardware components
- [x] Assemble robot

## Possible issues:
- If you encounter issues related to empty databases, you should add entries using registration (for users and staffs) and
cli_staff.py (for books and rooms). You can also just launch cli_staff.py right after you launch the server to load all the default entries into the database
