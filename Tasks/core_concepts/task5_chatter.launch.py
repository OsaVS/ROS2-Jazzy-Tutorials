from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    # create a Node using some parameters
    return LaunchDescription([

        # chatter node/ remap 'chatter' to 'test/chatter'
        Node(
            package="tests",
            executable="chatter.py",
            name="test_chatter",
            output="screen",
            remappings=[('/chatter', '/test/chatter')]
        ),

        # listener node
        Node(
            package="tests",
            executable="listener.py",
            name="listener",
            output="screen",
        ),

        # run shell commands or external programs
        ExecuteProcess(
            cmd=[
                'ros2', 'topic', 'pub', '--once', # publish once
                '/twist', 'geometry_msgs/Twist',  # topic and message type
                '{linear: {x: 0.0, y: 0.0., z: 0.0}, angular:{x: 0.0, y: 0.0, z: 0.00}}' # message
            ],
            output='screen'
        )
    ])