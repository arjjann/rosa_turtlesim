import os
import subprocess
import time

os.system("ros2 run turtlesim turtlesim_node")
time.sleep(2)
os.system("ros2 run turtlesim turtle_teleop_key")

