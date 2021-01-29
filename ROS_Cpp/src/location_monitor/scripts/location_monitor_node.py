#!/home/ricardo/.platformio/penv/bin/python3

import math
import rospy 
from nav_msgs.msg import Odometry 
from location_monitor.msg import LandmarkDistance

def distance(x1, y1, x2, y2):
    xd = x1 - x2
    yd = y1 - y2
    return math.sqrt(xd*xd + yd*yd)

class LandmarkMonitor(object):
    def __init__(self, pub, landmarks):
        self._pub = pub
        self._landmarks = landmarks

    def callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        
        closest_name = None
        closest_distance = None
        for l_name, l_x, l_y in self._landmarks:
            dist = distance(x, y, l_x, l_y)
            if closest_distance is None or dist < closest_distance:
                closest_name = l_name
                closest_distance = dist
        ld = LandmarkDistance()
        ld.name = closest_name
        ld.distance = closest_distance
        self._pub.publish(ld)
        if closest_distance < 0.5:
            rospy.loginfo('I\'m near the {}'.format(closest_name))
        #rospy.loginfo('closest, {}'.format(closest_name))
        #rospy.loginfo('x, {}, y: {}'.format(x, y))       

def main():
    rospy.init_node('location_monitor')

    landmarks = []
    landmarks.append(("Cylinder_11", -1.1, -1.1));
    landmarks.append(("Cylinder_12", -1.1, 0.0));
    landmarks.append(("Cylinder_13", -1.1, 1.1));
    landmarks.append(("Cylinder_21", 0.0, -1.1));
    landmarks.append(("Cylinder_22", 0.0, 0.0));
    landmarks.append(("Cylinder_23", 0.0, 1.1));
    landmarks.append(("Cylinder_31", 1.1, -1.1));
    landmarks.append(("Cylinder_32", 1.1, 0.0));
    landmarks.append(("Cylinder_33", 1.1, 1.1));

    pub = rospy.Publisher('closest_landmark', LandmarkDistance, queue_size=10)
    monitor = LandmarkMonitor(pub, landmarks)

    rospy.Subscriber("/odom", Odometry, monitor.callback)
    rospy.spin()

if __name__ == '__main__':
    main()