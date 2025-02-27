cmake_minimum_required(VERSION 3.5)
project(service_interface)

find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/Calc.srv"
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()