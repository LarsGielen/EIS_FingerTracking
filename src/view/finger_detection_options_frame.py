import tkinter as tk
from tkinter import ttk
from view.sliderentrywidget import SliderEntryWidget

class FingerDetectionSettingsFrame(ttk.Frame):
    def __init__(self, parent, update_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.update_callback = update_callback

        ttk.Label(self, text="Brightness Threshold:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.brightness_slider = SliderEntryWidget(self, initial_value=200, minmax=(0, 255), clamp_int=True)
        self.brightness_slider.grid(row=0, column=1, pady=10, sticky="w")
        self.brightness_slider.bind_on_change(self.on_param_change)

        ttk.Label(self, text="Min Radius:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.min_radius_slider = SliderEntryWidget(self, initial_value=5, minmax=(1, 50), clamp_int=True)
        self.min_radius_slider.grid(row=1, column=1, pady=10, sticky="w")
        self.min_radius_slider.bind_on_change(self.on_param_change)

        ttk.Label(self, text="Max Radius:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.max_radius_slider = SliderEntryWidget(self, initial_value=50, minmax=(1, 100), clamp_int=True)
        self.max_radius_slider.grid(row=2, column=1, pady=10, sticky="w")
        self.max_radius_slider.bind_on_change(self.on_param_change)

        ttk.Label(self, text="Param1:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.param1_slider = SliderEntryWidget(self, initial_value=50, minmax=(1, 255), clamp_int=True)
        self.param1_slider.grid(row=3, column=1, pady=10, sticky="w")
        self.param1_slider.bind_on_change(self.on_param_change)

        ttk.Label(self, text="Param2:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.param2_slider = SliderEntryWidget(self, initial_value=30, minmax=(1, 100), clamp_int=True)
        self.param2_slider.grid(row=4, column=1, pady=10, sticky="w")
        self.param2_slider.bind_on_change(self.on_param_change)

    def on_param_change(self):
        if self.update_callback is not None:
            self.update_callback(
                brightness_threshold=self.brightness_slider.get_value(),
                min_radius=self.min_radius_slider.get_value(),
                max_radius=self.max_radius_slider.get_value(),
                param1=self.param1_slider.get_value(),
                param2=self.param2_slider.get_value()
            )

    def get(self):
        return self.brightness_slider.get_value(), self.min_radius_slider.get_value(), self.max_radius_slider.get_value(), self.param1_slider.get_value(), self.param2_slider.get_value()
