import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from std_msgs.msg import String
from example_interfaces.srv import AddTwoInts
import sys
import time

class UniversalNode(Node):
    def __init__(self, mode):
        super().__init__(f'universal_node_{mode}')
        self.mode = mode

        # Define a QoS Profile for demonstration
        # BEST_EFFORT means messages might be dropped if network is congested
        # KEEP_LAST with depth 1 means only the most recent message is stored
        # VOLATILE durability means messages are not persisted
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            history=HistoryPolicy.KEEP_LAST,
            depth=1,
            durability=DurabilityPolicy.VOLATILE
        )

        if self.mode == 'publisher':
            self.publisher_ = self.create_publisher(String, 'topic', qos_profile)
            self.i = 0
            self.timer = self.create_timer(1.0, self.timer_callback)
            self.get_logger().info(f'Publisher node "{self.get_name()}" started. Publishing on topic "topic".')
        elif self.mode == 'subscriber':
            self.subscription = self.create_subscription(String, 'topic', self.listener_callback, qos_profile)
            self.get_logger().info(f'Subscriber node "{self.get_name()}" started. Subscribing to topic "topic".')
        elif self.mode == 'server':
            self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)
            self.get_logger().info(f'Service server node "{self.get_name()}" started. Service: "add_two_ints".')
        elif self.mode == 'client':
            self.cli = self.create_client(AddTwoInts, 'add_two_ints')
            while not self.cli.wait_for_service(timeout_sec=1.0):
                self.get_logger().info('service not available, waiting again...')
            self.req = AddTwoInts.Request()
            self.get_logger().info(f'Service client node "{self.get_name()}" started. Service: "add_two_ints".')
        else:
            self.get_logger().error(f'Invalid mode: {mode}')
            sys.exit(1)

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello ROS 2! Count: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f'Incoming request: a: {request.a} b: {request.b}')
        self.get_logger().info(f'Sending response: {response.sum}')
        return response

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)

    if len(sys.argv) < 2:
        print("Usage: python ros2_basics_example.py <mode> [args]")
        print("Modes: publisher, subscriber, server, client")
        rclpy.shutdown()
        return

    mode = sys.argv[1]
    node = UniversalNode(mode)

    try:
        if mode == 'client':
            if len(sys.argv) < 4:
                node.get_logger().error("Usage for client: python ros2_basics_example.py client <int_a> <int_b>")
                node.destroy_node()
                rclpy.shutdown()
                return
            a = int(sys.argv[2])
            b = int(sys.argv[3])
            node.send_request(a, b)
            
            while rclpy.ok():
                rclpy.spin_once(node)
                if node.future.done():
                    try:
                        response = node.future.result()
                    except Exception as e:
                        node.get_logger().error(f'Service call failed %r' % (e,))
                    else:
                        node.get_logger().info(f'Result of add_two_ints: for {a} + {b} = {response.sum}')
                    break
                time.sleep(0.1) # Small sleep to prevent busy-waiting
        else:
            rclpy.spin(node)
    except KeyboardInterrupt:
        pass # Allow graceful exit on Ctrl+C
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
