#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2021, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    robot_ip = LaunchConfiguration('robot_ip')
    hw_ns = LaunchConfiguration('hw_ns', default='ufactory')
    add_gripper = LaunchConfiguration('add_gripper', default='false')
    add_vacuum_gripper = LaunchConfiguration('add_vacuum_gripper', default='false')
    add_camera_adapter = LaunchConfiguration('add_camera_adapter', default='false')
    camera_adapter_xyz = LaunchConfiguration('camera_adapter_xyz', default='"0 0 0"')
    camera_adapter_rpy = LaunchConfiguration('camera_adapter_rpy', default='"0 0 0"')
    camera_adapter_tool_xyz = LaunchConfiguration('camera_adapter_tool_xyz', default='"0 0 0.0015"')
    camera_adapter_tool_rpy = LaunchConfiguration('camera_adapter_tool_rpy', default='"0 0 0"')
    no_gui_ctrl = LaunchConfiguration('no_gui_ctrl', default='false')

    # robot moveit realmove launch
    # xarm_moveit_config/launch/_robot_moveit_realmove.launch.py
    robot_moveit_realmove_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([FindPackageShare('xarm_moveit_config'), 'launch', '_robot_moveit_realmove.launch.py'])),
        launch_arguments={
            'robot_ip': robot_ip,
            'dof': '6',
            'robot_type': 'lite',
            'hw_ns': hw_ns,
            'add_gripper': add_gripper,
            'add_vacuum_gripper': add_vacuum_gripper,
            'add_camera_adapter': add_camera_adapter,
            'camera_adapter_xyz': camera_adapter_xyz,
            'camera_adapter_rpy': camera_adapter_rpy,
            'camera_adapter_tool_xyz': camera_adapter_tool_xyz,
            'camera_adapter_tool_rpy': camera_adapter_tool_rpy,
            'no_gui_ctrl': no_gui_ctrl,
        }.items(),
    )
    
    return LaunchDescription([
        robot_moveit_realmove_launch
    ])
