import cv2

def get_camera_list():
    available_cameras = []
    for i in range(5): 
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            available_cameras.append(i)
            cap.release()
    return available_cameras

def start_camera(camera_index):
    cap = cv2.VideoCapture(camera_index)
    return cap

def get_frame(cap):
    ret, frame = cap.read()
    if not ret:
        return None
    return frame

def release_camera(cap):
    cap.release()
