#!/usr/bin/env python3

import rospy
import cv2

def main():
    rospy.init_node("camera_viewer_node")
    rospy.loginfo("Starting camera viewer...")

    # Open the default camera (index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        rospy.logerr("Failed to open camera.")
        return

    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            rospy.logwarn("Failed to grab frame.")
            continue

        cv2.imshow("Camera Feed", frame)

        # 1ms wait for 'q' key or GUI response
        if cv2.waitKey(1) & 0xFF == ord('q'):
            rospy.loginfo("Quitting viewer...")
            break

        rate.sleep()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
