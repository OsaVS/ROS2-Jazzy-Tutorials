import rclpy
from rclpy.node import Node

class ParamsSetter(Node):
    def __init__(self):
        super().__init__('params_setter')  # Initialize node with name
        
        # Declare parameters with default values (empty strings)
        self.declare_parameter('param', '')  # Parameter name to set
        self.declare_parameter('value', '')  # Value to assign
        
        # Retrieve the parameters
        param_name = self.get_parameter('param').value
        param_value = self.get_parameter('value').value  
        
        # Set the global ROS parameter
        self.set_parameters([
            rclpy.parameter.Parameter(
                param_name,
                rclpy.Parameter.Type.STRING, 
                param_value
            )
        ])
        
        # Log confirmation
        self.get_logger().info(f'Set parameter "{param_name}" to "{param_value}"')

def main(args=None):
    rclpy.init(args=args)
    node = ParamsSetter()
    rclpy.spin(node)  # Keep node alive
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()