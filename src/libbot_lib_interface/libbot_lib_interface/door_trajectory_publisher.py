import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration

class TrajectoryPublisherNode(Node):
    def __init__(self):
        super().__init__('trajectory_publisher_node')

        # Declare and get parameters (for better configurability)
        self.declare_parameter('input_topic', '/door_control')
        self.declare_parameter('output_topic', '/joint_trajectory_controller/joint_trajectory')
        self.declare_parameter('joint_name', 'door_joint')
        self.declare_parameter('time_from_start_sec', 3)

        self.input_topic = self.get_parameter('input_topic').get_parameter_value().string_value
        self.output_topic = self.get_parameter('output_topic').get_parameter_value().string_value
        self.joint_name = self.get_parameter('joint_name').get_parameter_value().string_value
        self.time_from_start_sec = self.get_parameter('time_from_start_sec').get_parameter_value().integer_value

        # Subscriber to the input topic
        self.subscription = self.create_subscription(
            Float64,
            self.input_topic,
            self.position_callback,
            10
        )

        # Publisher for the trajectory message
        self.publisher = self.create_publisher(JointTrajectory, self.output_topic, 10)
        self.get_logger().info('Trajectory Publisher Node has been started.')

    def position_callback(self, msg: Float64):
        position = msg.data
        self.get_logger().info(f'Received position: {position}')

        # Create and publish the JointTrajectory message
        trajectory_msg = JointTrajectory()
        trajectory_msg.joint_names = [self.joint_name]

        # Define a trajectory point with the received position
        point = JointTrajectoryPoint()
        point.positions = [position]
        point.time_from_start = Duration(sec=self.time_from_start_sec)

        trajectory_msg.points = [point]

        self.publisher.publish(trajectory_msg)
        self.get_logger().info(f'Published trajectory with position: {position}')


def main(args=None):
    rclpy.init(args=args)
    node = TrajectoryPublisherNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Node stopped by user')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
