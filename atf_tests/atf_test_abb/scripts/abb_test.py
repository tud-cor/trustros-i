import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg


moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial',anonymous=True)


group = moveit_commander.MoveGroupCommander("manipulator")


pose_target = geometry_msgs.msg.Pose()
pose_target.position.x = 0.732
pose_target.position.y = 0.0
pose_target.position.z = 1.325
pose_target.orientation.w = 1.0
group.set_pose_target(pose_target)
group.go(wait=True)


rospy.sleep(2)
pose_target.position.x = 1.140
pose_target.position.y = 0.0
pose_target.position.z = 0.725
pose_target.orientation.w = 1.0
group.set_pose_target(pose_target)
group.go(wait=True)


rospy.sleep(2)
pose_target.position.x = 0.0
pose_target.position.y = 1.140
pose_target.position.z = 0.725
pose_target.orientation.w = 1.0
group.set_pose_target(pose_target)
group.go(wait=True)


rospy.sleep(2)
pose_target.position.x = 0.0
pose_target.position.y = -1.140
pose_target.position.z = 0.725
pose_target.orientation.w = 1.0
group.set_pose_target(pose_target)
group.go(wait=True)
