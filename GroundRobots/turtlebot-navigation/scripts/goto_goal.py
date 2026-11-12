import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
import math
import sys

class GoToGoal(Node):
    def __init__(self):
        super().__init__('goto_goal')
        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        self.goal_x = 0.0
        self.goal_y = 0.0
        self.goal_set = False
        self.reached = False
        self.has_position = False
        self.x_min = 0
        self.x_max = 5.5
        self.y_min = -2
        self.y_max = 2.1
        self.cmd_pub = self.create_publisher(Twist, '/commands/velocity', 10)
        self.create_subscription(Odometry, '/marvelmind_odom', self.odom_callback, 10)
        self.create_timer(0.1, self.control_loop)
        self.get_logger().info('GoToGoal node started!')

    def odom_callback(self, msg):
        self.has_position = True
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        q = msg.pose.pose.orientation
        siny_cosp = 2.0 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
        self.yaw = math.atan2(siny_cosp, cosy_cosp)

    def control_loop(self):
        if not self.has_position:
            return
        if not self.goal_set or self.reached:
            return

        dx = self.goal_x - self.x
        dy = self.goal_y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance < 0.15:
            self.get_logger().info('Goal reached!')
            self.stop()
            self.reached = True
            return

        angle_to_goal = math.atan2(dy, dx)
        angle_error = angle_to_goal - self.yaw

        while angle_error > math.pi:
            angle_error -= 2.0 * math.pi
        while angle_error < -math.pi:
            angle_error += 2.0 * math.pi

        cmd = Twist()
        # If heading error exceeds ~25 deg, turn in place toward the goal
        if abs(angle_error) > 0.45:
            # Clamp in-place turn rate
            ang_speed = max(-0.4, min(0.4, 0.6 * angle_error))
            cmd.angular.z = float(ang_speed)
            cmd.linear.x = 0.0
        else:
            # Drive forward while making fine heading adjustments
            cmd.linear.x = float(min(0.2, 0.3 * distance))
            cmd.angular.z = float(max(-0.4, min(0.4, 0.4 * angle_error)))

        self.get_logger().info(
            f'Pos: ({self.x:.2f}, {self.y:.2f}) | '
            f'Yaw: {math.degrees(self.yaw):.1f}° | '
            f'GoalYaw: {math.degrees(angle_to_goal):.1f}° | '
            f'Err: {math.degrees(angle_error):.1f}° | '
            f'CmdZ: {cmd.angular.z:.2f}'
        )
        self.cmd_pub.publish(cmd)

    def stop(self):
        self.cmd_pub.publish(Twist())

    def set_goal(self, gx, gy):
        if (gx < self.x_min or gx > self.x_max or
            gy < self.y_min or gy > self.y_max):
            self.get_logger().error(f'Goal x={gx}, y={gy} is outside boundary! Rejected.')
            return
        self.goal_x = gx
        self.goal_y = gy
        self.goal_set = True
        self.reached = False
        self.get_logger().info(f'Goal set: x={gx}, y={gy}')

def main(args=None):
    rclpy.init(args=args)
    node = GoToGoal()
    if len(sys.argv) == 3:
        gx = float(sys.argv[1])
        gy = float(sys.argv[2])
        node.set_goal(gx, gy)
        node.get_logger().info(f'Driving to x={gx}, y={gy}')
    else:
        node.get_logger().info('Usage: goto_goal <goal_x> <goal_y>')
        node.get_logger().info('Example: goto_goal 2.0 -1.5')
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
