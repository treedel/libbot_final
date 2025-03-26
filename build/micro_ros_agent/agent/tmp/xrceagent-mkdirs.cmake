# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/home/devesh/Butterfly/project_2/libbot_final/build/micro_ros_agent/agent/src/xrceagent"
  "/home/devesh/Butterfly/project_2/libbot_final/build/micro_ros_agent/agent/src/xrceagent-build"
  "/home/devesh/Butterfly/project_2/libbot_final/install/micro_ros_agent"
  "/home/devesh/Butterfly/project_2/libbot_final/build/micro_ros_agent/agent/tmp"
  "/home/devesh/Butterfly/project_2/libbot_final/build/micro_ros_agent/agent/src/xrceagent-stamp"
  "/home/devesh/Butterfly/project_2/libbot_final/build/micro_ros_agent/agent/src"
  "/home/devesh/Butterfly/project_2/libbot_final/build/micro_ros_agent/agent/src/xrceagent-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/home/devesh/Butterfly/project_2/libbot_final/build/micro_ros_agent/agent/src/xrceagent-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/home/devesh/Butterfly/project_2/libbot_final/build/micro_ros_agent/agent/src/xrceagent-stamp${cfgdir}") # cfgdir has leading slash
endif()
