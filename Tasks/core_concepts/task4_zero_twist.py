import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class ZeroTwist(Node):
    def __init__(self):
        super().__init__('zero_twist')

        self.subscription = self.create_subscription(String, 'is_stopped', self.callback, 10)

        self.publisher = self.create_publisher(Twist, 'twist', 10)

        self.zero_message = Twist()
        self.zero_message.linear.x = 0.0
        self.zero_message.linear.y = 0.0
        self.zero_message.linear.z = 0.0
        self.zero_message.angular.x = 0.0
        self.zero_message.angular.y = 0.0
        self.zero_message.angular.z = 0.0

    def callback(self, message):
        if message.data.lower() == "true":
            self.publisher.publish(self.zero_message)
            self.get_logger().info(f"{self.zero_message}")
            return
        
    
def main(args=None):
    rclpy.init(args=args)
    node = ZeroTwist()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()