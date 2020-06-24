import tkinter as tk
from tkinter import ttk


class CreateProject(ttk.Frame):
    def __init__(self, parent, controller, show_settings):
        super().__init__(parent)

        self["style"] = "Background.TFrame"

        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        self.current_timer_label = tk.StringVar(value=self.controller.timer_schedule[0])
        self.current_time = tk.StringVar(value=f"{controller.github_api_token.get()}")
    
        settings_button = ttk.Button(
            self,
            text="Settings",
            command=show_settings,
            style="PomodoroButton.TButton",
            cursor="hand2"
        )

        settings_button.grid(row=0, column=1, sticky="E", padx=10, pady=(10, 0))
        
        button_container = ttk.Frame(self, style="Background.TFrame")
        button_container.grid(sticky="EW", padx=10, pady=10, columnspan=2)
        button_container.columnconfigure(0, weight=1)
        
        create_project = ttk.Button(
            button_container,
            text="Create Project",
            style="PomodoroButton.TButton",
            cursor="hand2"  # hand1 in some systems
        )

        create_project.grid(column=0, row=0, sticky="EW", padx=2)
    
