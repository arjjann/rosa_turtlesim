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
    return subprocess.Popen(["ros2","run","turtlesim","turtlesim_node"])

class CommandTurtle(Node):
    def __init__(self):
        super().__init__("command_turtle")
        self.pub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
    
    def send(self, lin=0.0, ang=0.0):
            msg=Twist()
            msg.linear.x=float(lin)
            msg.angular.z=float(ang)
            self.pub.publish(msg)
launch=launch_turtlesim()
time.sleep(2)
rclpy.init()
commander=CommandTurtle()

@tool
def move_forward(distance: float)->str:
    """This move turtle forward or backward by the used defined unit."""
    speed=1.0
    if distance > 0:
        direction=speed
    else:
        direction=-speed
    
    duration=abs(distance/speed)
    dt=0.1
    ltime=0.0

    while ltime < duration:
        commander.send(lin=direction)
        time.sleep(dt)
        ltime+=dt
    commander.send(0,0)

    return f"turtle moved by {distance}"

@tool
def turn(angle: float)->str:
    """Turn by the defined angle where positive is anticlockwise."""
    speed=1.0
    radians=math.radians(abs(angle))
    if angle > 0:
        direction=speed
    else:
        direction=-speed

    duration=(radians)/speed
    dt=0.1
    rotate_time=0.0

    while rotate_time < duration:
        commander.send(ang=direction)
        time.sleep(dt)
        rotate_time+=abs(direction)*dt
    commander.send(0,0)

    return f"turtle rotated by {angle} degree"

@tool
def circle(radius: float)-> str:
    """Make one complete circle with given radius in meter"""
    linear_speed=1.0
    angular_speed=linear_speed/radius
    duration=(2*3.1415*radius)/linear_speed
    dt=0.1
    rotate_time=0.0
    while rotate_time <= duration:
        commander.send(lin=linear_speed, ang=angular_speed)
        time.sleep(dt)
        rotate_time+=angular_speed*0.1

    commander.send(0,0)
    return f"completed a circle of radius {radius} meter"

prompts= RobotSystemPrompts(
    embodiment_and_persona=(
        "You control a Turtlesim robot."
        "You can move fordward/backward, Turn and make a circle"
        "you can combine action of robot"
    )
)

agent= ROSA( ros_version=2, llm=azure_llm, tools=[move_forward,turn, circle], prompts=prompts)

print("LLM Turtle controller is runnning .\n enter 'q' for exit")

while True:
    cmd=input("Give command to control a robot:")
    if cmd.lower()=='q':
        break
    print("Robot",agent.invoke(cmd))

rclpy.shutdown()   
launch.terminate() 
    