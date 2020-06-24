import tkinter as tk
from tkinter import ttk


class Settings(ttk.Frame):
    def __init__(self, parent, controller, show_timer):
        super().__init__(parent)

        self["style"] = "Background.TFrame"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        settings_container = ttk.Frame(
            self,
            padding="30 15 30 15",
            style="Background.TFrame"
        )

        settings_container.grid(row=0, column=0, sticky="EW", padx=10, pady=10)

        settings_container.columnconfigure(0, weight=1)
        settings_container.rowconfigure(1, weight=1)

        github_api_token = ttk.Label(
            settings_container,
            text="Gitub api token: ",
            style="LightText.TLabel"
        )
        github_api_token.grid(column=0, row=0, sticky="W")

        github_api_token_input = tk.Entry(
            settings_container,
            justify="center",
            textvariable=controller.github_api_token,
            width=10,
        )
        github_api_token_input.grid(column=1, row=0, sticky="EW")
        github_api_token_input.focus()

        default_venv_name = ttk.Label(
            settings_container,
            text="Default venv name: ",
            style="LightText.TLabel"
        )
        default_venv_name.grid(column=0, row=1, sticky="W")

        default_ven_input = tk.Entry(
            settings_container,
            justify="center",
            textvariable=controller.default_venv_name,
            width=10,
        )
        default_ven_input.grid(column=1, row=1, sticky="EW")

        short_break_label = ttk.Label(
            settings_container,
            text="Short break time: ",
            style="LightText.TLabel"
        )
        short_break_label.grid(column=0, row=2, sticky="W")

        short_break_input = tk.Entry(
            settings_container,
            justify="center",
            textvariable=controller.short_break,
            width=10,
        )
        short_break_input.grid(column=1, row=2, sticky="EW")

        for child in settings_container.winfo_children():
            child.grid_configure(padx=5, pady=5)
        
        button_container = ttk.Frame(self, style="Background.TFrame")
        button_container.grid(sticky="EW", padx=10)
        button_container.columnconfigure(0, weight=1)

        timer_button = ttk.Button(
            button_container,
            text="← Back",
            command=show_timer,
            style="PomodoroButton.TButton",
            cursor="hand2"  # hand1 in some systems
        )

        timer_button.grid(column=0, row=0, sticky="EW", padx=2)