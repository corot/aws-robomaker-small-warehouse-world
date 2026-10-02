cmake_minimum_required(VERSION 3.10)
project(aws_robomaker_small_house_world)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch models worlds maps photos routes
  DESTINATION share/${PROJECT_NAME}
)

# Make the models available to Gazebo as model://<name> once the workspace is sourced
ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/hooks/${PROJECT_NAME}.dsv.in")

ament_package()
