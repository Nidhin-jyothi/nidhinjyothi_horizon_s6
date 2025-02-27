TurtleBot Controller
Overview
This project demonstrates a ROS 2-based TurtleBot Controller using the turtlesim package. It utilizes a publisher-subscriber model where:

The TurtleBot's movement is controlled based on its position.

The bot moves at different speeds based on its location.

The pen color changes dynamically when crossing a specific x-coordinate.

Features
Uses a subscriber to read the TurtleBot's pose (/turtle1/pose).

Publishes velocity commands (/turtle1/cmd_vel) to control movement.

Calls a service (/turtle1/set_pen) to change the pen color dynamically.

The TurtleBot turns at the boundaries to stay within the area.

Prerequisites
Ensure you have the following installed:

ROS 2 Humble (or compatible version)

turtlesim package

Installation
Create a ROS 2 workspace and navigate inside it:

mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
Clone the repository inside the src directory:

git clone <your-repo-url>
Go back to the workspace root and build the package:

cd ~/ros2_ws
colcon build
Source the workspace:

source install/setup.bash
Running the Project
Step 1: Start the turtlesim node
ros2 run turtlesim turtlesim_node
Step 2: Run the Turtle Controller Node
ros2 run my_robot_controller turtle_controller.py
How It Works
The TurtleBot moves faster in the central area and turns at the boundaries.

When crossing x = 5.5, the pen color switches between red and green.

Uses ROS 2 topics and services for movement and color change.

Files
turtle_controller.py: Main ROS 2 node for controlling the TurtleBot.

package.xml: Defines dependencies for the ROS 2 package.

setup.py: ROS 2 package setup file.

Conclusion
This project is a simple demonstration of ROS 2's capabilities using turtlesim. It highlights subscribers, publishers, and services in a practical scenario.
