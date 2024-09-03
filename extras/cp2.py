from picamera2 import Picamera2
import cv2
import time

def capture_camera1():
    picam1 = Picamera2(1)
    
    # Configure the camera
    config = picam1.create_still_configuration() # sets up default parameters optimized for taking single, high-quality images
    picam1.configure(config) 
    
    # Start the camera
    picam1.start()
    
    # Wait for the camera to warm up
    time.sleep(2)
    
    # Capture an image
    frame_1 = picam1.capture_array()
    
    # Stop the camera
    picam1.stop()
    
    # Save the image
    cv2.imwrite("cap_img.jpg", cv2.cvtColor(frame_1, cv2.COLOR_RGB2BGR))
    
    return "cap_img.jpg"