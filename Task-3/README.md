# ACTION AND SERVICE

## A: Ubuntu Installation via Dual Boot
Ubuntu has been installed via dual boot. 

## B: ROS 2 Humble Installation
ROS 2 Humble has been installed. 

## C: Services - Basic Calculator
A ROS 2 service has been implemented to perform basic calculations. The default operation is addition. The service files are located in the respective folder.

### Creating a ROS 2 Workspace
Create a ROS 2 workspace and navigate inside it:
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```

Clone the repository inside the `src` directory:
```bash
git clone https://github.com/Nidhin-jyothi/nidhinjyothi_horizon_s6.git
```

Go back to the workspace root and build the package:
```bash
cd ~/ros2_ws
colcon build
```

Source the workspace:
```bash
source install/setup.bash
```

### Running the Service
1. Start the ROS 2 service node:
   ```bash
   ros2 run service calc_server
   ```
2. Call the service:
   ```bash
   ros2 run service calc_client
   ```

### Video
[Watch the demo](https://drive.google.com/file/d/10AzWJNAQFJA1g6KXBoArXmbiw8yOnt7t/view?usp=drive_link)   

## D: Actions - Counting Action
A ROS 2 action has been implemented to count until a target number with a defined period. The action files are located in the respective folder.

### Running the Action
1. Start the action server:
   ```bash
   ros2 run action_py count_until_server
   ```
2. Call the action:
   ```bash
   ros2 run action_py count_until_client
   ```

### Video
[Watch the demo](https://drive.google.com/file/d/1vsCdGFlvOXB9hj8k_ME0ir2EDSujOMpD/view?usp=drive_link)  
