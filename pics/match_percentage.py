import cv2
import numpy as np
#import serial
import time

# Open serial port
#ser = serial.Serial('COM8', 9600)  # Change 'COM1' to your serial port
#time.sleep(2)  # Wait for the serial connection to establish

# Function to compute match percentage and send over serial
def get_match_percentage(image1, image2):
    # Load images
    img1 = cv2.imread(image1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image2, cv2.IMREAD_GRAYSCALE)

    # Initiate ORB detector
    orb = cv2.ORB_create()

    # Find keypoints and descriptors
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # Create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors
    matches = bf.match(des1, des2)

    # Sort them in the order of their distance
    matches = sorted(matches, key=lambda x: x.distance)

    # Compute match percentage
    num_good_matches = len(matches)
    total_matches = min(len(kp1), len(kp2))
    match_percentage = (num_good_matches / total_matches) * 100
    
    # Send match percentage over serial
    #ser.write(str(int(match_percentage)).encode())

    return match_percentage

# Paths to the images you want to compare
image1_path = 'ref1.jpg'
image2_path = 'img3ed.jpg'

# Compute and send match percentage
match_percentage = get_match_percentage(image1_path, image2_path)
print("Match Percentage:", match_percentage)

# Close serial port
#ser.close()
