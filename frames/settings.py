import tkinter as tk
from tkinter import ttk
import json, os


class Settings(ttk.Frame):
    def __init__(self, parent, controller, show_project):
        super().__init__(parent)

        self["style"] = "Background.TFrame"

        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.dir_path = os.path.dirname(os.path.abspath(__file__))

        user_label = ttk.Label(
            self,
            text="Username or Email adress: ",
            style="LightText.TLabel"
        )
        user_label.grid(column=0, row=0, sticky="W")

        username_input = tk.Entry(
            self,
            justify="center",
            textvariable=controller.username,
            width=16,
            font=("TkDefaultFont", 15)
        )
        username_input.grid(column=1, row=0, sticky="E")

        password_label = ttk.Label(
            self,
            text="Password: ",
            style="LightText.TLabel"
        )
        password_label.grid(column=0, row=1, sticky="W")

        password = tk.Entry(
            self,
            show="*",
            justify="center",
            textvariable=controller.password,
            width=16,
            font=("TkDefaultFont", 15)
        )
        password.grid(column=1, row=1, sticky="E")

        default_venv_name = ttk.Label(
            self,
            text="Virtual Env name: ",
            style="LightText.TLabel"
        )
        default_venv_name.grid(column=0, row=2, sticky="W")

        default_ven_input = tk.Entry(
            self,
            justify="center",
            textvariable=controller.default_venv_name,
            width=16,
            font=("TkDefaultFont", 15)
        )
        default_ven_input.grid(column=1, row=2, sticky="EW")

        back_button = ttk.Button(
            self,
            text="← Back",
            command=lambda: [show_project(), self.update_settings()],
            style="Button.TButton",
            cursor="hand2"  # hand1 in some systems
        )
        back_button.grid(columnspan=2, row=3, sticky="EW")


        for child in self.winfo_children():
            child.grid_configure(padx=14, pady=14)

    def update_settings(self):
        """Update settings with given input fields"""
        os.chdir(self.dir_path)
        venv_name = self.controller.default_venv_name.get().strip()
        username = self.controller.username.get().strip()
        password = self.controller.password.get().strip()

        if not venv_name:
            self.controller.default_venv_name.set("venv")
            venv_name = "venv"

        with open("settings.json", "w") as f:
            data = {"username": username, "password": password, "default_venv_name": venv_name}
            json.dump(data, f)

