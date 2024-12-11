import time
import numpy as np

class FingerMovementTracker:
    def __init__(self, single_click_timeout=.3, double_click_timeout=0.5, slide_threshold=20):
        self.prev_finger_positions = []

        self.delta_callback = None

        self.last_click_time = None
        self.single_click_timeout = single_click_timeout
        self.single_click_callback = None

    def set_delta_callback(self, callback):
        self.delta_callback = callback

    def set_single_click_callback(self, callback):
        self.single_click_callback = callback

    def set_double_click_callback(self, callback):
        self.double_click_callback = callback

    def set_double_finger_slide_callback(self, callback):
        self.double_finger_slide_callback = callback

    def calculate_finger_delta(self, current_finger_positions):
        deltas = []

        if len(self.prev_finger_positions) == 0:
            self.prev_finger_positions = current_finger_positions
            return deltas

        for current_finger in current_finger_positions:
            cx, cy, _ = current_finger

            closest_match_idx = None
            min_distance = float('inf')

            for i, prev_finger in enumerate(self.prev_finger_positions):
                px, py, _ = prev_finger
                distance = np.sqrt((cx - px) ** 2 + (cy - py) ** 2)

                if distance < min_distance:
                    min_distance = distance
                    closest_match_idx = i

            if closest_match_idx is not None:
                px, py, _ = self.prev_finger_positions[closest_match_idx]
                delta_x = cx - px
                delta_y = cy - py
                deltas.append((delta_x, delta_y))

        if len(deltas) > 0 and self.delta_callback: self.delta_callback(deltas)

        self.prev_finger_positions = current_finger_positions
        return deltas

    def detect_single_click(self, current_finger_positions, time_now):
        if len(current_finger_positions) == 1:
            if self.last_click_time is None:
                self.last_click_time = time_now
                return

        if len(current_finger_positions) == 0 and self.last_click_time:
            if (time_now - self.last_click_time) <= self.single_click_timeout:
                if self.single_click_callback:
                    self.single_click_callback()
            self.last_click_time = None

    def update(self, current_finger_positions):
        time_now = time.time()
        deltas = self.calculate_finger_delta(current_finger_positions)
        self.detect_single_click(current_finger_positions, time_now)

