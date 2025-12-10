import os
import subprocess
import time
from langchain.agents import tool
from rosa import ROSA, RobotSystemPrompts
from llm import azure_llm
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

def launch_turtlesim():
    return subprocess.Popen(["ros2", "run", "turtlesim", "turtlesim_node"])

class CommandTurtle(Node):
    def __init__(self):
        super().__init__("command_turtle")
        self.pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

    def send(self, lin=0.0, ang=0.0):
        msg = Twist()
        msg.linear.x = float(lin)
        msg.angular.z = float(ang)
        self.pub.publish(msg)

# Launch sim
launch = launch_turtlesim()
time.sleep(2)
rclpy.init()
commander = CommandTurtle()

# --------------------------
# FIXED move_forward
# --------------------------
@tool
def move_forward(distance: float) -> str:
    """Move forward or backward accurately."""
    speed = 1.0  # m/s
    direction = speed if distance > 0 else -speed

    total_time = abs(distance / speed)
    dt = 0.1
    elapsed = 0.0

    while elapsed < total_time:
        commander.send(lin=direction)
        time.sleep(dt)
        elapsed += dt

    commander.send(0, 0)
    return f"Turtle moved {distance} meters"


# --------------------------
# FIXED turn (degrees)
# --------------------------
@tool
def turn(angle: float) -> str:
    """Turn accurately in degrees."""
    ang_speed = 1.0  # rad/s
    radians = math.radians(abs(angle))

    direction = ang_speed if angle > 0 else -ang_speed

    dt = 0.1
    rotated = 0.0

    while rotated < radians:
        commander.send(ang=direction)
        time.sleep(dt)
        rotated += abs(direction) * dt

    commander.send(0, 0)
    return f"Turtle rotated {angle} degrees"


# --------------------------
# FIXED circle
# --------------------------
@tool
def circle(radius: float) -> str:
    """Draw a perfect circle by controlling angle over time."""
    linear_speed = 1.0
    angular_speed = linear_speed / radius

    total_angle = 2 * math.pi
    dt = 0.1
    rotated = 0.0

    while rotated < total_angle:
        commander.send(lin=linear_speed, ang=angular_speed)
        time.sleep(dt)
        rotated += angular_speed * dt

    commander.send(0, 0)
    return f"Completed a circle of radius {radius} meters"


# LLM Setup
prompts = RobotSystemPrompts(
    embodiment_and_persona=(
        "You control a Turtlesim robot. "
        "You can move forward/backward, turn, and make circles. "
        "You can combine actions."
    )
)

agent = ROSA(ros_version=2, llm=azure_llm, tools=[move_forward, turn, circle], prompts=prompts)

print("LLM Turtle controller running.\nEnter 'q' to exit.\n")

while True:
    cmd = input("Give command to control robot: ")
    if cmd.lower() == 'q':
        break
    print("Robot:", agent.invoke(cmd))

rclpy.shutdown()
launch.terminate()
