import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose

class PoseRePublisher(Node):
    def __init__(self):
        super().__init__('pose_re_pub')

        # subscribe to topic pose_with_covariance_stamped
        self.subscription = self.create_subscription(PoseWithCovarianceStamped, 'pose_with_covariance_stamped', self.callback, 10)

        #publish to topic pose
        self.publisher = self.create_publisher(Pose, 'pose', 10)

    #call back function: publish a pose message when a pose_with_covariance_stamped message is received using the pose message included in it
    def callback(self, message):
        pose = message.pose.pose
        self.publisher.publish(pose)


def main(args=None):
    rclpy.init(args=args)
    node = PoseRePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()   

if __name__== '__main__':
    main()