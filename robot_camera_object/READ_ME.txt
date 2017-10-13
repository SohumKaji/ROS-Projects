###########
# READ ME #
#####################
# PROJECT: robot_camera_object #
#$###################

>> This ROS project 
- subscribes to a 'two_ints' topic and receives two integers
- finds the sum of the two integers
- publishes the sum to the topic 'sum'
- I only wrote code to perform the above tasks, the environment and 'two_ints' topic publishing were provided.

>>The code that I worked on can be found in:
- catkin_ws/src/project1_solution/scripts/solution.py
- This includes subscribing to 'two_ints', finding the sum, and publishing to the 'sum' topic

>> The two_ints topic publishing code can be found in:
- catkin_ws/src/two_int_talker/scripts/two_int_talker.py
- This was part of the provided code

To setup/run project for yourself:
Run: 
source setup_project1.sh
rosrun project1_solution solution.py

