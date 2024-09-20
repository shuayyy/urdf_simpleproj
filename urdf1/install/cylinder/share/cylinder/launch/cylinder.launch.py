import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Define the path to the URDF file
    package_dir = get_package_share_directory('cylinder')
    urdf_file = os.path.join(package_dir, 'urdf', 'cylinder.urdf')

    # Check if the URDF file exists (optional but helpful for debugging)
    if not os.path.exists(urdf_file):
        raise FileNotFoundError(f"URDF file not found: {urdf_file}")

    # Return the LaunchDescription for RViz and robot_state_publisher
    return LaunchDescription([
        # Publish the URDF to the 'robot_description' parameter
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}]
        ),
        # Start RViz
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
        ),
    ])
