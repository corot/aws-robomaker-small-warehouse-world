# AWS RoboMaker Small House World ROS package

ROS 2 Jazzy / Gazebo Harmonic version of the AWS RoboMaker small house world.

![Gazebo01](docs/images/gazebo_01.png)

**Visit the [AWS RoboMaker website](https://aws.amazon.com/robomaker/) to learn more about building intelligent robotic applications with Amazon Web Services.**

# Include the world from another package

* Add this repository to your workspace `.repos` file and run `vcs import src < your.repos`
```yaml
repositories:
  aws-robomaker-small-house-world:
    type: git
    url: https://github.com/corot/aws-robomaker-small-warehouse-world.git
    version: thorp
```
* Add the following to your launch file:
```python
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

# Launch World
world = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(
        get_package_share_directory('aws_robomaker_small_house_world') + '/launch/small_house.launch.py'),
    launch_arguments={'gui': 'true'}.items(),
)
```

`small_house.launch.py` starts Gazebo (server only unless `gui:=true`) and bridges the simulation clock to `/clock`.
Sourcing the workspace adds this package's `models` folder to `GZ_SIM_RESOURCE_PATH`, so Gazebo can resolve the `model://` URIs.

# Load directly into Gazebo (without ROS)
```bash
export GZ_SIM_RESOURCE_PATH=`pwd`/models
gz sim worlds/small_house.world
```

# ROS Launch with Gazebo viewer (without a robot)
```bash
# build for ROS
rosdep install --from-paths . --ignore-src -r -y
colcon build

# run in ROS
source install/setup.sh
ros2 launch aws_robomaker_small_house_world view_small_house.launch.py
```

# Building
Include this as a `.repos` dependency in your simulation workspace. `colcon build` will build this repository.

To build it outside an application, note there is no robot workspace. It is a simulation workspace only.

```bash
$ vcs import src < your.repos
$ rosdep install --from-paths src --ignore-src -r -y
$ colcon build
```

# How to Replace Photos in Picture Frames

Picture frames use two textures for the model:
 - `aws_portraitA_01.png` - Frame texture
 - `aws_portraitA_02.png` - Picture texture

To change a picture, one has to replace the `aws_portraitA_02.png` file. The new image will look best with same aspect ratio as the replaced image.

Below is a table showing portrait type to picture resolution data and custom images from photos/.

| Portrait Model | Resolution | Photo |
| --- | --- | --- |
| DeskPortraitA_01 | 650x1024 | |
| DeskPortraitA_02 | 650x1024 | doug |
| DeskPortraitB_01 | 650x1024 | |
| DeskPortraitB_02 | 650x1024 | |
| DeskPortraitC_01 | 1024x1024 | |
| DeskPortraitC_02 | 1024x1024 | |
| DeskPortraitD_01 | 1024x1024 | |
| DeskPortraitD_02 | 1024x1024 | |
| DeskPortraitD_03 | 1024x1024 | |
| DeskPortraitD_04 | 1024x1024 | ray |
| PortraitA_01 | 700x1024 | tim |
| PortraitA_02 | 700x1024 | anamika |
| PortraitB_01 | 700x1024 | renato |
| PortraitB_02 | 700x1024 | brandon |
| PortraitB_03 | 700x1024 | miaofei |
| PortraitC_01 | 650x1024 | sean |
| PortraitD_01 | 1024x450 | |
| PortraitD_02 | 1024x450 | |
| PortraitE_01 | 700x1024 | maggie |
| PortraitE_02 | 700x1024 | iftach |

# Disclaimer

All objects in the scene should be static objects as intended for this sample app.
If there is a need for some of objects to be non-static, change their 'static' flag in the world file to 'false', 
and make sure they have correct mass and inertia values in their model.sdf
Link: http://gazebosim.org/tutorials?tut=inertia&cat=build_robot

Currently, objects in scene have inconsistent mass and inertia values, they will be fixed in the future change.
Inconsistent mass and inertia should not affect static object simulation.


