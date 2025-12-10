import subprocess
import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
def launch_turtlesim():
    return subprocess.Popen(["ros2","run","turtlesim","turtlesim_node"])

class CircleMover(Node):
    def __init__(self):
        super().__init__('circle_mover')
        self.publisher=self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer= self.create_timer(0.1, self.move_circle)

    def move_circle(self):
        msg=Twist()
        msg.linear.x= 1.0
        msg.angular.z= 0.8
        self.publisher.publish(msg)

def main():
    print("Here turtlesim is launching..")
    proc=launch_turtlesim()
    time.sleep(1.5)
    rclpy.init()
    node =CircleMover()

    print("Moving the turtle in a circle ....")
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
    
    print("closing turtlesim..")
    proc.terminate()

if __name__=='__main__':
    main()
