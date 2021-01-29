#include "ros/ros.h"
#include "location_monitor/LandmarkDistance.h"
#include "landmark_monitor.h"

using location_monitor::LandmarkDistance;

int main(int argc, char** argv) {

    // Initialize node called /location_monitor
    ros::init(argc, argv, "location_monitor");

    ros::NodeHandle nh;

    // Publishing message type LandmarkDistance to a topic called /closest_landmark
    ros::Publisher landmark_pb = nh.advertise<LandmarkDistance>("closest_landmark", 10);

    LandmarkMonitor monitor(landmark_pb);
    // Subscribing to /odom topic called closest_landmark
    ros::Subscriber sub = nh.subscribe("odom", 10, &LandmarkMonitor::OdomCallback, &monitor);
    
    ros::spin();
    return 0; 
}