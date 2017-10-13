#!/usr/bin/env python  
import rospy

import numpy

import tf
import tf2_ros
import geometry_msgs.msg

def publish_transforms():
 
    ############################
    #Base Frame to Object Frame# 
    ############################
    T1 = numpy.dot(tf.transformations.quaternion_matrix(tf.transformations.quaternion_from_euler(.79, 0, .79)), tf.transformations.translation_matrix((0.0, 1.0, 1.0)))
  
 
    object_transform = geometry_msgs.msg.TransformStamped()
    object_transform.header.stamp = rospy.Time.now()
    object_transform.header.frame_id = "base_frame"
    object_transform.child_frame_id = "object_frame"
        
    q1 = tf.transformations.quaternion_from_matrix(T1)
    object_transform.transform.rotation.x = q1[0]
    object_transform.transform.rotation.y = q1[1]
    object_transform.transform.rotation.z = q1[2]
    object_transform.transform.rotation.w = q1[3]
    
    tr1 = tf.transformations.translation_from_matrix(T1)
    object_transform.transform.translation.x = tr1[0]
    object_transform.transform.translation.y = tr1[1]
    object_transform.transform.translation.z = tr1[2]
    
    br.sendTransform(object_transform)
    
    
    ###########################
    #Base Frame to Robot Frame#
    ###########################
    
    R2 = tf.transformations.rotation_matrix(1.5, (0, 0, 1))
    
    T2 = numpy.dot(tf.transformations.quaternion_matrix(tf.transformations.quaternion_from_matrix(R2)), tf.transformations.translation_matrix((0.0, -1.0, 0.0)))

    
    robot_transform = geometry_msgs.msg.TransformStamped()
    robot_transform.header.stamp = rospy.Time.now()
    robot_transform.header.frame_id = "base_frame"
    robot_transform.child_frame_id = "robot_frame"
    
    
    
    q2 = tf.transformations.quaternion_from_matrix(T2)
    robot_transform.transform.rotation.x = q2[0]
    robot_transform.transform.rotation.y = q2[1]
    robot_transform.transform.rotation.z = q2[2]
    robot_transform.transform.rotation.w = q2[3]
    
    tr2 = tf.transformations.translation_from_matrix(T2)
    robot_transform.transform.translation.x = tr2[0]
    robot_transform.transform.translation.y = tr2[1]
    robot_transform.transform.translation.z = tr2[2]
        
    br.sendTransform(robot_transform)
    
   
    #############################
    #Robot Frame to Camera Frame#
    #############################
    
    T2_inverse = tf.transformations.inverse_matrix(T2)
    #T2_inverse[0][3] = 1
    #T2_inverse[1][3] = 1
    #T2_inverse[2][3] = 1
    #T2_inverse[3][3] = 1
    
    T1_final = T1
    #T1_final[0][3] = 1
    #T1_final[1][3] = 1
    #T1_final[2][3] = 1
    #T1_final[3][3] = 1
    
    
    tr1 = numpy.append(tr1, [1])
    #print(tr1)
    T3 = numpy.dot(T2_inverse, T1_final) 
    #print(T3)
    #T4 = numpy.dot(T3, tf.transformations.translation_matrix(tr1))
    
    tv_c_o = tf.transformations.translation_from_matrix(T3) - (0, 0.1, 0.1)
    #tv_c_o = tf.transformations.unit_vector(tv_c_o)
    
    angle = numpy.arccos(numpy.dot(tv_c_o, (1,0,0)))
    print(angle)
    axis = -1 * numpy.cross(tv_c_o,(1,0,0))    
    print(axis)
   
    """
    R4_x = tf.transformations.quaternion_about_axis(angle, axis)
    R4_y = tf.transformations.quaternion_about_axis(0, axis)
    R4_z = tf.transformations.quaternion_about_axis(0, axis)
    
    R4_q = tf.transformations.quaternion_multiply(R4_x, R4_y)
    R4_q = tf.transformations.quaternion_multiply(R4_q, R4_z)
    R4 = tf.transformations.quaternion_matrix(R4_q)
    """
    R4 = tf.transformations.rotation_matrix(angle, axis) #tf.transformations.quaternion_about_axis(angle, axis) #tf.transformations.rotation_matrix(angle, axis)
    
    #T4 = numpy.dot(tf.transformations.quaternion_matrix(tf.transformations.quaternion_from_matrix(R4)), tf.transformations.translation_matrix((0, 0.1, 0.1)))
 
    camera_transform = geometry_msgs.msg.TransformStamped()
    camera_transform.header.stamp = rospy.Time.now()
    camera_transform.header.frame_id = "robot_frame"
    camera_transform.child_frame_id = "camera_frame"
    
    
    q3 = tf.transformations.quaternion_from_matrix(R4)
    camera_transform.transform.rotation.x = q3[0]
    camera_transform.transform.rotation.y = q3[1]
    camera_transform.transform.rotation.z = q3[2]
    camera_transform.transform.rotation.w = q3[3]
    
    #tr3 = tf.transformations.translation_from_matrix(T4)
    camera_transform.transform.translation.x = 0 #tr3[0]
    camera_transform.transform.translation.y = .1 #tr3[1]
    camera_transform.transform.translation.z = 0.1 #tr3[2]
    
    
    br.sendTransform(camera_transform)

if __name__ == '__main__':
    rospy.init_node('project2_solution')

    br = tf2_ros.TransformBroadcaster()
    rospy.sleep(0.5)

    while not rospy.is_shutdown():
        publish_transforms()
        rospy.sleep(0.05)
