import cv2

import rclpy
from sensor_msgs.msg import Image
from rclpy.node import Node
from cv_bridge import CvBridge

class ImagePublisherNode(Node):
    
    def __init__(self):
        
        super().__init__('image_publisher')

        self.declare_parameter('camera_device', 0)
        self.camera_device = self.get_parameter('camera_device').value
        self.camera = cv2.VideoCapture(self.camera_device, cv2.CAP_V4L2)

        self.topic = "image"
        self.queue_size = 20
        self.publisher = self.create_publisher(Image, self.topic, self.queue_size)

        self.bridge = CvBridge()

        self.publish_rate = 30.0
        self.timer = self.create_timer(1/self.publish_rate, self.timer_callback)

    def timer_callback(self):

        ret, frame = self.camera.read()

        if ret:
            frame = cv2.resize(frame, (820, 640), interpolation=cv2.INTER_CUBIC)
            img_msg = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            self.publisher.publish(img_msg)

def main():

    rclpy.init()

    image_publisher = ImagePublisherNode()
    rclpy.spin(image_publisher)

    image_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()