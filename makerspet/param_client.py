import rclpy
from makerspet.robot import ParamClient

# The following is just to start the node
def main(args=None):
  rclpy.init(args=args)
  param_client = ParamClient('pet')

  # rclpy.spin(node)
  param_client.destroy_node()
  rclpy.shutdown()

# ros2 run makerspet robot
if __name__ == "__main__":
  main()
