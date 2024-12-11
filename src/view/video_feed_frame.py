import tkinter as tk
from PIL import Image, ImageTk
import cv2

class VideoFeedView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=640, height=480)
        self.canvas.pack()

    def show_video_feed(self, frame):
        if frame is not None:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            img_tk = ImageTk.PhotoImage(image=img)
            self.canvas.create_image(0, 0, anchor="nw", image=img_tk)
            self.canvas.image = img_tk 

    def start_video_feed(self, cap):
        while True:
            ret, frame = cap.read()
            if ret:
                self.show_video_feed(frame)
            else:
                break
