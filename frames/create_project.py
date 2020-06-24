import tkinter as tk
from tkinter import ttk


class CreateProject(ttk.Frame):
    def __init__(self, parent, controller, show_settings):
        super().__init__(parent)

        self["style"] = "Background.TFrame"

        self.controller = controller
        self.columnconfigure(0, weight=1)
    
        settings_button = ttk.Button(
            self,
            text="Settings",
            command=show_settings,
            style="Button.TButton",
            cursor="hand2"
        )
        settings_button.grid(row=0, column=1, sticky="E")
        
        create_project = ttk.Button(
            self,
            text="Create Project",
            style="Button.TButton",
            cursor="hand2"  # hand1 in some systems
        )
        create_project.grid(row=1, columnspan=2, sticky="EW")


        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)