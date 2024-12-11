import tkinter as tk

import view.finger_detection_options_frame as finger_detection_options_frame
import view.camera_search_frame as camera_search_frame
import view.video_feed_frame as video_feed_frame
import model.camera_model as camera
import model.finger_detection_model as finger_detection
import model.finger_movement_model as finger_movement
import model.simulate_keyboard_model as simulate_keyboard

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Camera Viewer")

        self.finger_detection_options = finger_detection_options_frame.FingerDetectionSettingsFrame(self, None)
        self.finger_detection_options.pack(padx=10, pady=10)

        self.video_feed_view = video_feed_frame.VideoFeedView(self)
        self.video_feed_view.pack(padx=10, pady=10)

        self.camera_search_view = camera_search_frame.CameraSearchView(self, on_camera_selected=self.on_camera_selected)
        self.camera_search_view.pack(padx=10, pady=10)

        self.current_camera = None

        self.movement_tracker = finger_movement.FingerMovementTracker()
        self.movement_tracker.set_delta_callback(lambda deltas: simulate_keyboard.move_mouse(deltas[0][0], deltas[0][1]))
        self.movement_tracker.set_single_click_callback(lambda: simulate_keyboard.click_mouse())

    def on_camera_selected(self, selected_camera):
        if self.current_camera:
            camera.release_camera(self.current_camera)

        self.current_camera = camera.start_camera(int(selected_camera))
        self.update()

    def update(self):
        frame = camera.get_frame(self.current_camera)
        finger_locations = finger_detection.detect_finger_tops(frame, *self.finger_detection_options.get())

        self.movement_tracker.update(finger_locations)

        frame = finger_detection.draw_circles_on_image(frame, finger_locations)
        if frame is not None: self.video_feed_view.show_video_feed(frame)
        self.after(10, self.update)

if __name__ == "__main__":
    app = App()
    app.mainloop()
