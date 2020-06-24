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

        github_api_token = ttk.Label(
            self,
            text="Gitub api token: ",
            style="LightText.TLabel"
        )
        github_api_token.grid(column=0, row=0, sticky="W")

        github_api_token_input = tk.Entry(
            self,
            justify="center",
            textvariable=controller.github_api_token,
            width=16,
            font=("TkDefaultFont", 14)
        )
        github_api_token_input.grid(column=1, row=0, sticky="EW")
        github_api_token_input.focus()

        default_venv_name = ttk.Label(
            self,
            text="Virtual Env name: ",
            style="LightText.TLabel"
        )
        default_venv_name.grid(column=0, row=1, sticky="W")

        default_ven_input = tk.Entry(
            self,
            justify="center",
            textvariable=controller.default_venv_name,
            width=16,
            font=("TkDefaultFont", 14)
        )
        default_ven_input.grid(column=1, row=1, sticky="EW")

        back_button = ttk.Button(
            self,
            text="← Back",
            command=lambda: [show_project(), self.update_settings()],
            style="Button.TButton",
            cursor="hand2"  # hand1 in some systems
        )
        back_button.grid(columnspan=2, row=2, sticky="EW", padx=2)


        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=12)

    def update_settings(self):
        """Update settings with given input fields"""
        os.chdir(self.dir_path)
        venv_name = self.controller.default_venv_name.get()
        github_token = self.controller.github_api_token.get()
        print(venv_name, github_token)
        with open("settings.json", "w") as f:
            data = {"github_api_token": github_token, "default_venv_name": venv_name}
            json.dump(data, f)

