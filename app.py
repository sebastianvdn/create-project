import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from frames import CreateProject, Settings
import json

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"


class Project(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Background.TFrame", background=COLOUR_PRIMARY)

        style.configure("CreateProject.TFrame", background=COLOUR_LIGHT_BACKGROUND)

        style.configure(
            "LightText.TLabel",
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT,
        )

        style.configure(
            "LightText.TCheckbutton",
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT,
        )

        style.map(
            "LightText.TCheckbutton",
            background=[("active", COLOUR_PRIMARY), ("disabled", COLOUR_PRIMARY)]
        )

        style.configure(
            "Button.TButton",
            background=COLOUR_SECONDARY,
            foreground=COLOUR_LIGHT_TEXT,
        )

        style.map(
            "Button.TButton",
            background=[("active", COLOUR_PRIMARY), ("disabled", COLOUR_LIGHT_TEXT)]
        )

        style.configure("TProgressbar", background='green')
    
        # Main app window is a tk widget, so background is set directly
        self["background"] = COLOUR_PRIMARY
        self.title("Create a new Project")
        self.columnconfigure(0, weight=1)

        # Set the overall fontsize to 15 instead of 10.
        font.nametofont("TkDefaultFont").configure(size=14)

        # try to open existing settings file and create one if it does not exist
        data = self.get_settings()
        self.username = tk.StringVar(value=data["username"])
        self.password = tk.StringVar(value=data["password"])
        self.default_venv_name = tk.StringVar(value=data["default_venv_name"])
        self.folder_path = tk.StringVar(value="C:/")
        self.create_venv = tk.BooleanVar()
        self.project_name = tk.StringVar()
        self.progress_int_var = tk.IntVar()

        container = ttk.Frame(self)
        container.grid()

        self.frames = {}

        settings_frame = Settings(container, self, lambda: self.show_frame(CreateProject))
        project_frame = CreateProject(container, self, lambda: self.show_frame(Settings))
        settings_frame.grid(row=0, column=0, sticky="NESW")
        project_frame.grid(row=0, column=0, sticky="NESW")

        self.frames[Settings] = settings_frame
        self.frames[CreateProject] = project_frame
        
        self.show_frame(CreateProject)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

    def get_settings(self):
        """
        get settings or create new one
        """
        try:
            with open("frames\\settings.json") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open('frames\\settings.json', 'w') as f:
                data = {"username": "", "password": "", "default_venv_name": "venv"}
                json.dump(data, f)
        return data

app = Project()
app.iconbitmap('github-logo.ico')
app.mainloop()