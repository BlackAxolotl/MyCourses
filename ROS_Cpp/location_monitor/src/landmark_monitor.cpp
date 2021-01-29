#include "landmark_monitor.h"

LandmarkMonitor::LandmarkMonitor(const ros::Publisher& landmark_pub) 
        : landmarks_(), landmark_pub_(landmark_pub){                
            InitLandmarks();
    }

// Function that computes the closest landmark around the robot
LandmarkDistance LandmarkMonitor::FindClosest(double x, double y) {
    LandmarkDistance result;
    result.distance = -1;

    for (size_t i = 0; i < landmarks_.size(); ++i) {
        const Landmark& landmark = landmarks_[i];
        double xDistance = landmark.x - x;
        double yDistance = landmark.y - y;
        double distance = sqrt(xDistance*xDistance + yDistance*yDistance);

        if (result.distance < 0 || distance < result.distance) {
            result.name = landmark.name;
            result.distance = distance;
        }
    }

    return result;
}

// Callback function used to subscribe to /Odom topic (gazebo robot coordinates)
// Callback function used to publish LandmarkMessage to new /closest_landmark topic (my robot info coordinates)
void LandmarkMonitor::OdomCallback(const nav_msgs::Odometry::ConstPtr& msg) {
    double x = msg->pose.pose.position.x;
    double y = msg->pose.pose.position.y;
    LandmarkDistance ld = FindClosest(x, y);

    // Publishing LandmarkMessage
    landmark_pub_.publish(ld);

    // Printing out in terminal information
    if (ld.distance <= 0.5) {
        ROS_INFO("I am near the %s", ld.name.c_str());
    }        
} 

// Pushback all the landmarks have to be considered in the FindClosest function
// All this landmark coordinates were obtained directly looking into Model/ros_symbol/symbol in Gazeboo 
// Property/visual/pose (all nine Property/geometry/CYLINDER)
void LandmarkMonitor::InitLandmarks() {
    landmarks_.push_back(Landmark("Cylinder_11", -1.1, -1.1));
    landmarks_.push_back(Landmark("Cylinder_12", -1.1, 0.0));
    landmarks_.push_back(Landmark("Cylinder_13", -1.1, 1.1));
    landmarks_.push_back(Landmark("Cylinder_21", 0.0, -1.1));
    landmarks_.push_back(Landmark("Cylinder_22", 0.0, 0.0));
    landmarks_.push_back(Landmark("Cylinder_23", 0.0, 1.1));
    landmarks_.push_back(Landmark("Cylinder_31", 1.1, -1.1));
    landmarks_.push_back(Landmark("Cylinder_32", 1.1, 0.0));
    landmarks_.push_back(Landmark("Cylinder_33", 1.1, 1.1));
}