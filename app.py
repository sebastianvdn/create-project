import tkinter as tk
from tkinter import ttk
from collections import deque
from frames import CreateProject, Settings
from ctypes import windll
import json
windll.shcore.SetProcessDpiAwareness(1)


COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"


class Project(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("CreateProject.TFrame", background=COLOUR_LIGHT_BACKGROUND)
        style.configure("Background.TFrame", background=COLOUR_PRIMARY)
        style.configure(
            "TimerText.TLabel",
            background=COLOUR_LIGHT_BACKGROUND,
            foreground=COLOUR_DARK_TEXT,
            font="Courier 38"
        )

        style.configure(
            "LightText.TLabel",
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT,
        )

        style.configure(
            "PomodoroButton.TButton",
            background=COLOUR_SECONDARY,
            foreground=COLOUR_LIGHT_TEXT,
        )

        style.map(
            "PomodoroButton.TButton",
            background=[("active", COLOUR_PRIMARY), ("disabled", COLOUR_LIGHT_TEXT)]
        )

        # Main app window is a tk widget, so background is set directly
        self["background"] = COLOUR_PRIMARY

        self.title("Create a new Project")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        with open("settings.json") as f:
            data = json.load(f)
        self.github_api_token = tk.StringVar(value=data["github_api_token"])
        self.default_venv_name = tk.StringVar(value=data["default_venv_name"])
        self.timer_order = [
            "Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro", "Long Break"
            ]
        self.timer_schedule = deque(self.timer_order)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        self.frames = {}

        settings_frame = Settings(container, self, lambda: self.show_frame(CreateProject))
        timer_frame = CreateProject(container, self, lambda: self.show_frame(Settings))
        settings_frame.grid(row=0, column=0, sticky="NESW")
        timer_frame.grid(row=0, column=0, sticky="NESW")

        self.frames[Settings] = settings_frame
        self.frames[CreateProject] = timer_frame
        
        self.show_frame(CreateProject)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


app = Project()
app.mainloop()