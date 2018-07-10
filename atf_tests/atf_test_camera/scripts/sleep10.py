#!/usr/bin/python
import unittest
import rospy
import rostest
import sys

from atf_core import ATF


class Application:
    def __init__(self):
        self.atf = ATF()

    def execute(self):
	
        # Make sure all hardware is up and running (mainly needed for ensenso)
        # did not use the ATF wait for topic since this interferes with testing the interface
        rospy.sleep(30) 
	
        # ROS Camera test
        self.atf.start("get_data")
        rospy.sleep(10)
        self.atf.stop("get_data")
	
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
