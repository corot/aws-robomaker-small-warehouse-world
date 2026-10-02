import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node


def generate_launch_description():
    world = os.path.join(get_package_share_directory('aws_robomaker_small_house_world'),
                         'worlds', 'small_house.world')

    # Always set GUI to false for AWS RoboMaker Simulation
    # Use gui:=true on ros2 launch command-line to run with a gui.
    gui = LaunchConfiguration('gui')
    server_only = PythonExpression(["'' if '", gui, "'.lower() in ('true', '1') else '-s'"])

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')),
        launch_arguments={
            'gz_args': ['-r -v 3 ', server_only, ' ', world],
            'on_exit_shutdown': 'true',
        }.items(),
    )

    # Publish simulation time on /clock, as gazebo_ros used to do
    clock_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='clock_bridge',
        arguments=['/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock'],
        output='screen',
    )

    return LaunchDescription([
        DeclareLaunchArgument('gui', default_value='false', description='Run Gazebo GUI'),
        gazebo,
        clock_bridge,
    ])
