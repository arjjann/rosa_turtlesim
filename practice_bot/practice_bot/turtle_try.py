import os
import subprocess
import time
import 

node_process=subprocess.Popen(["ros2","run","turtlesim","turtlesim_node"])
# os.system("ros2 run turtlesim turtlesim_node")
time.sleep(2)

teleop_process=subprocess.Popen(["ros2","run","turtlesim","turtle_teleop_key"])
# os.system("ros2 run turtlesim turtle_teleop_key")
circle=subprocess.Popen()
node_process.wait()
teleop_process.wait()