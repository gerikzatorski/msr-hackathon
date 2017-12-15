#!/usr/bin/env python
import numpy as np
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Point
from detection_algos import detect

class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("servo_commands",Point,queue_size=10)
    self.image_sub = rospy.Subscriber("usb_cam/image_raw",Image,self.callback)
    self.bridge = CvBridge()

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print("==[CAMERA MANAGER]==", e)

    (rows,cols,channels) = cv_image.shape

    # Circle Detection
    center = detect(cv_image)
    # print center
    # print "--------------"
    deltas = Point()
    deltas.x = center.x - 320
    deltas.y = 240 - center.y
    deltas.z = 0
    
    # Publish to servo motor
    self.image_pub.publish(deltas)
    cv2.waitKey(1)
    # cv2.waitKey(3)
"""
    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)
"""
def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
