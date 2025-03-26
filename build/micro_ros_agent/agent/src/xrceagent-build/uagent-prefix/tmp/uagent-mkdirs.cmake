# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/home/devesh/Butterfly/project_2/libbot_final/build/micro_ros_agent/agent/src/xrceagent"
  "/home/devesh/Butterfly/project_2/libbot_final/build/micro_ros_agent/agent/src/xrceagent-build"
  "/home/devesh/Butterfly/project_2/libbot_final/build/micro_ros_agent/agent/src/xrceagent-build/uagent-prefix"
  "/home/devesh/Butterfly/project_2/libbot_final/build/micro_ros_agent/agent/src/xrceagent-build/uagent-prefix/tmp"
  "/home/devesh/Butterfly/project_2/libbot_final/build/micro_ros_agent/agent/src/xrceagent-build/uagent-prefix/src/uagent-stamp"
  "/home/devesh/Butterfly/project_2/libbot_final/build/micro_ros_agent/agent/src/xrceagent-build/uagent-prefix/src"
  "/home/devesh/Butterfly/project_2/libbot_final/build/micro_ros_agent/agent/src/xrceagent-build/uagent-prefix/src/uagent-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/home/devesh/Butterfly/project_2/libbot_final/build/micro_ros_agent/agent/src/xrceagent-build/uagent-prefix/src/uagent-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/home/devesh/Butterfly/project_2/libbot_final/build/micro_ros_agent/agent/src/xrceagent-build/uagent-prefix/src/uagent-stamp${cfgdir}") # cfgdir has leading slash
endif()
