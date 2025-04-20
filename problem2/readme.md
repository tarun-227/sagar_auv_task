# ROS Python Nodes – Description

This set of ROS nodes demonstrates a simple data-processing pipeline using `std_msgs/Int32` messages and a separate OpenCV-based camera viewer.

---

## 🧩 Node 1: `multiples_of_2`

### 📌 Description:
Publishes increasing **multiples of 2** every second on the `/multiples_of_2` topic.

### 📤 Publishes:
- Topic: `/multiples_of_2`
- Type: `std_msgs/Int32`

### 🔁 Behavior:
- Starts from 2 (2 × 1)
- Increments the multiplier each second
- Publishes: 2, 4, 6, 8, ...

---

## 🧩 Node 2: `multiplier_node`

### 📌 Description:
Subscribes to `/multiples_of_2`, multiplies the number by **10**, and publishes the result to `/times_10`.

### 📥 Subscribes:
- Topic: `/multiples_of_2`
- Type: `std_msgs/Int32`

### 📤 Publishes:
- Topic: `/times_10`
- Type: `std_msgs/Int32`

### 🔁 Behavior:
- Input: 2 → Output: 20  
- Input: 4 → Output: 40  
- And so on...

---

## 🧩 Node 3: `adder_node`

### 📌 Description:
Subscribes to `/times_10`, **adds 5** to the received number, and logs the result using `rospy.loginfo()`.

### 📥 Subscribes:
- Topic: `/times_10`
- Type: `std_msgs/Int32`

### 🧠 Behavior:
- Input: 20 → Log: 25  
- Input: 40 → Log: 45

### 📤 Publishes:
- **None**

---

## 🎥 Node 4: `camera_viewer_node`

### 📌 Description:
A standalone node that opens the webcam and displays the **live video feed** using OpenCV.

### 📷 Dependencies:
- OpenCV (`cv2`)
- No ROS topics used

### 🔁 Behavior:
- Opens camera using `cv2.VideoCapture(0)`
- Displays real-time video in a window
- Quits when the **'q'** key is pressed

---

## 🔗 Overall Node Communication Flow

```text
[multiples_of_2]
       |
       v
 /multiples_of_2
       |
       v
[multiplier_node]
       |
       v
   /times_10
       |
       v
   [adder_node]
