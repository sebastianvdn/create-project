import tkinter as tk
from tkinter import ttk


class Timer(ttk.Frame):
    def __init__(self, parent, controller, show_settings):
        super().__init__(parent)

        self["style"] = "Background.TFrame"

        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        self.current_timer_label = tk.StringVar(value=self.controller.timer_schedule[0])
        self.current_time = tk.StringVar(value=f"{controller.github_api_token.get()}:00")
        self.timer_running = False
        self._timer_decrement_job = None

        settings_button = ttk.Button(
            self,
            text="Settings",
            command=show_settings,
            style="PomodoroButton.TButton",
            cursor="hand2"
        )

        settings_button.grid(row=0, column=1, sticky="E", padx=10, pady=(10, 0))

        timer_description = ttk.Label(
            self,
            textvariable=self.current_timer_label,
            style="LightText.TLabel"
        )
        timer_description.grid(row=0, column=0, sticky="W", padx=(10, 0), pady=(10, 0))

        timer_frame = ttk.Frame(self, height="100", style="Timer.TFrame")
        timer_frame.grid(row=1, column=0, columnspan=2, pady=(10, 0), sticky="NSEW")

        timer_counter = ttk.Label(
            timer_frame,
            textvariable=self.current_time,
            style="TimerText.TLabel"
        )
        timer_counter.place(relx=0.5, rely=0.5, anchor="center")

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
    
