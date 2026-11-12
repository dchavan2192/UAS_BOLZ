#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster
from marvelmind_ros2_msgs.msg import HedgePositionAngle

# Forward zero reference captured earlier
ZERO_OFFSET_DEG = 82.3

def hedgehog_angle_to_yaw(angle_deg: float, offset_deg: float) -> float:
    # Adding 180 deg (math.pi) flips the paired-beacon vector from backward to forward
    corrected_deg = angle_deg - offset_deg
    yaw_rad = math.radians(corrected_deg) + math.pi
    return (yaw_rad + math.pi) % (2.0 * math.pi) - math.pi

class MarvelmindPairedLocalizationNode(Node):
    def __init__(self):
        super().__init__('marvelmind_fusion')

        self.declare_parameter('zero_offset_deg', ZERO_OFFSET_DEG)
        self.offset = self.get_parameter('zero_offset_deg').get_parameter_value().double_value

        self.odom_pub = self.create_publisher(Odometry, '/marvelmind_odom', 10)
        self.tf_broadcaster = TransformBroadcaster(self)

        self.sub = self.create_subscription(
            HedgePositionAngle,
            '/hedgehog_pos_ang',
            self.pos_ang_callback,
            10
        )

        self.get_logger().info(
            f'Paired Marvelmind Node active. Zero offset: {self.offset:.2f} deg'
        )

    def pos_ang_callback(self, msg: HedgePositionAngle):
        yaw = hedgehog_angle_to_yaw(msg.angle, self.offset)
        now = self.get_clock().now().to_msg()

        qz = math.sin(yaw / 2.0)
        qw = math.cos(yaw / 2.0)

        # 1. MUST publish /marvelmind_odom for Nav2 controller_server
        odom = Odometry()
        odom.header.stamp = now
        odom.header.frame_id = 'map'
        odom.child_frame_id = 'base_footprint'
        odom.pose.pose.position.x = float(msg.x_m)
        odom.pose.pose.position.y = float(msg.y_m)
        odom.pose.pose.position.z = 0.0
        odom.pose.pose.orientation.x = 0.0
        odom.pose.pose.orientation.y = 0.0
        odom.pose.pose.orientation.z = qz
        odom.pose.pose.orientation.w = qw
        self.odom_pub.publish(odom)

        # 2. Dynamic map -> base_footprint transform
        t = TransformStamped()
        t.header.stamp = now
        t.header.frame_id = 'map'
        t.child_frame_id = 'base_footprint'
        t.transform.translation.x = float(msg.x_m)
        t.transform.translation.y = float(msg.y_m)
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = qz
        t.transform.rotation.w = qw
        self.tf_broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = MarvelmindPairedLocalizationNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
