import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    # Show Gazebo GUI on launch
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('aws_robomaker_small_house_world'),
                             'launch', 'small_house.launch.py')),
            launch_arguments={'gui': 'true'}.items(),
        ),
    ])
