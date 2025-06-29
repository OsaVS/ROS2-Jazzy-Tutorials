import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import os
import csv
from ament_index_python.packages import get_package_share_directory


class TwistFromDatabase(Node):
    def __init__(self):
        super().__init__('twist_from_database')

        self.publisher = self.create_publisher(Twist, 'twist_from_database', 20)

        self.values = self.load_twist_values()
        self.index = 0

        time_period = 0.1
        self.timer = self.create_timer(time_period, self.timer_callback)
        
    def load_twist_values(self):
        # extract the twist data values from the 'values.csv' file
        file_path = 'values.csv'

        # file can not be found
        if not os.path.isfile('/home/ovs/ros2_ws/src/core_concepts/values.csv'):
            self.get_logger().error(f"csv file not found: {file_path}")
            return []
        
        values = []
        with open('/home/ovs/ros2_ws/src/core_concepts/values.csv', 'r') as f:
            reader = csv.reader(f)

            for row in reader:
                # input with invalid length
                if len(row) != 6:
                     self.get_logger().warn(f"skipping incorrect input: {row}")
                     continue
                
                try:
                    row_values = [float(v.strip()) for v in row]
                    values.append(row_values)
                except:
                    # invalid input(data that can't be converted to float)
                    self.get_logger().warn(f"non-float input: {row}")

            return values
        
    def timer_callback(self):
        if self.index >= len(self.values):
            self.get_logger().info("All msgs published")
            return

        row = self.values[self.index]
        twist = Twist()
        twist.linear.x = row[0]
        twist.linear.y = row[1]
        twist.linear.z = row[2]
        twist.angular.x = row[3]
        twist.angular.y = row[4]
        twist.angular.z = row[5]

        self.publisher.publish(twist)
        self.get_logger().info("twist msg published: {twist}")
        self.index += 1

            
def main(args=None):
    rclpy.init(args=args)
    node = TwistFromDatabase()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
        
if __name__ == '__main__':
    main()

        