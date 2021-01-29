#pragma once

#include <vector>
#include <string>
#include <cmath>

#include "ros/ros.h"
#include "nav_msgs/Odometry.h"
#include "location_monitor/LandmarkDistance.h"
#include "landmark.h"

using std::vector;
using std::string;
using std::size_t;
using location_monitor::LandmarkDistance;

class LandmarkMonitor {

public:
    LandmarkMonitor(const ros::Publisher& landmark_pub);
    LandmarkDistance FindClosest(double x, double y);
    void OdomCallback(const nav_msgs::Odometry::ConstPtr& msg);

private:
    vector<Landmark> landmarks_;
    ros::Publisher landmark_pub_;

    void InitLandmarks();
};