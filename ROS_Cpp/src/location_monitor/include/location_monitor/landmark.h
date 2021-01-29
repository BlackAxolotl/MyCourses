#pragma once

#include <string>

using std::string;

class Landmark {
public:
    Landmark(string name, double x, double y)
        : name(name), x(x), y(y) {}

    string name;
    double x;
    double y;
};