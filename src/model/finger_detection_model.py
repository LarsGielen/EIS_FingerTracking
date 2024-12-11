import cv2
import numpy as np

def detect_finger_tops(image, brightness_threshold=200, min_radius=5, max_radius=50, param1=50, param2=30):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, brightness_threshold, 255, cv2.THRESH_BINARY)
    blurred = cv2.GaussianBlur(thresh, (13, 13), 2)

    detected_circles = []
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=param1, param2=param2, minRadius=min_radius, maxRadius=max_radius)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            detected_circles.append((x, y, r))
    
    return detected_circles

def draw_circles_on_image(image, circles):
    output_image = image.copy()

    for (x, y, r) in circles:
        cv2.circle(output_image, (x, y), r, (0, 255, 0), 4) 
        cv2.rectangle(output_image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    
    return output_image
