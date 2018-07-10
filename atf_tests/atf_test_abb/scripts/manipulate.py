#!/usr/bin/python
import unittest
import rospy
import rostest
import sys
import copy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

from atf_core import ATF

class Application:
    def __init__(self):
        self.atf = ATF()

        moveit_commander.roscpp_initialize(sys.argv)
        self.group = moveit_commander.MoveGroupCommander("manipulator")

    def execute(self):


        

        # dummy home
        self.atf.start("initialize")
        pose_target = geometry_msgs.msg.Pose()
        pose_target.position.x = 0.732
        pose_target.position.y = 0.0
        pose_target.position.z = 1.325
        pose_target.orientation.w = 1.0
        self.group.set_pose_target(pose_target)
        self.group.go()
        self.atf.stop("initialize")

        self.atf.start("full_test")

        # down
        self.atf.start("move_down")
        pose_target2 = geometry_msgs.msg.Pose()
        pose_target2.position.x = 1.140
        pose_target2.position.y = 0.0
        pose_target2.position.z = 0.825
        pose_target2.orientation.w = 1.0
        self.group.set_pose_target(pose_target2)
        self.group.go()
        self.atf.stop("move_down")

        # left
        self.atf.start("move_left")
        pose_target3 = geometry_msgs.msg.Pose()
        pose_target3.position.x = 0.0
        pose_target3.position.y = 1.140
        pose_target3.position.z = 0.825
        pose_target3.orientation.w = 1.0
        self.group.set_pose_target(pose_target3)
        self.group.go()
        self.atf.stop("move_left")

        # right
        self.atf.start("move_right")
        pose_target4 = geometry_msgs.msg.Pose()
        pose_target4.position.x = 0.0
        pose_target4.position.y = -1.140
        pose_target4.position.z = 0.825
        pose_target4.orientation.w = 1.0
        self.group.set_pose_target(pose_target4)
        self.group.go()
        self.atf.stop("move_right")

        # home
        self.atf.start("move_up")
        pose_target5 = geometry_msgs.msg.Pose()
        pose_target5.position.x = 0.732
        pose_target5.position.y = 0.0
        pose_target5.position.z = 1.325
        pose_target5.orientation.w = 1.0
        self.group.set_pose_target(pose_target5)
        self.group.go()
        self.atf.stop("move_up")

        self.atf.stop("full_test")

        self.atf.shutdown()

class Test(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def tearDown(self):
        pass

    def test_Recording(self):
        self.app.execute()

if __name__ == '__main__':
    rospy.init_node('test_name')
    if "standalone" in sys.argv:
        app = Application()
        app.execute()
    else:
        rostest.rosrun('application', 'recording', Test, sysargs=None)
