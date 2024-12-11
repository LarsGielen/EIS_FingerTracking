import tkinter as tk
from tkinter import ttk
import threading

import model.camera_model as camera

class CameraSearchView(tk.Frame):
    def __init__(self, master=None, on_camera_selected=None):
        super().__init__(master)
        self.master = master
        self.on_camera_selected = on_camera_selected 
        self.create_widgets()
        self.start_camera_search()

    def create_widgets(self):
        self.searching_label = tk.Label(self, text="Searching for cameras...", font=('Helvetica', 14))
        self.searching_label.pack(pady=10)

        self.camera_label = tk.Label(self, text="Select Camera:")
        self.camera_combobox = ttk.Combobox(self, state="readonly")
        self.start_button = tk.Button(self, text="Start Camera", command=self.start_video_feed)

    def start_camera_search(self):
        self.searching_label.pack()
        self.camera_label.pack_forget()
        self.camera_combobox.pack_forget()
        self.start_button.pack_forget()

        search_thread = threading.Thread(target=self.find_available_cameras)
        search_thread.daemon = True
        search_thread.start()

    def find_available_cameras(self):
        cameras = camera.get_camera_list() 
        self.master.after(0, self.update_camera_list, cameras) 

    def update_camera_list(self, cameras):
        self.searching_label.pack_forget()

        if cameras:
            self.camera_combobox['values'] = cameras
            self.camera_combobox.set(cameras[0]) 
            self.camera_label.pack(pady=10)
            self.camera_combobox.pack(pady=10)
            self.start_button.pack(pady=10)
        else:
            self.searching_label.config(text="No cameras found")
            self.searching_label.pack(pady=10)

    def start_video_feed(self):
        selected_camera = self.camera_combobox.get()
        if selected_camera and self.on_camera_selected:
            self.on_camera_selected(selected_camera)
