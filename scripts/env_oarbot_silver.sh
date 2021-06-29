#!/usr/bin/env bash

export ROS_WS=/home/oarbot_silver/catkin_ws
export ROS_KINETIC=/opt/ros/kinetic
source $ROS_KINETIC/setup.bash
source $ROS_WS/devel/setup.bash
export PATH=$ROS_ROOT/bin:$PATH
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$ROS_WS
export ROS_MASTER_URI=http://192.168.1.100:11311/
export ROS_IP=192.168.1.101
echo 1234 | sudo -S chmod 666 /dev/ttyACM0
echo 1234 | sudo -S chmod 666 /dev/ttyACM1
echo 1234 | sudo -S chmod 666 /dev/ttyACM2
echo 1234 | sudo -S chmod 666 /dev/ttyACM3

exec "$@"