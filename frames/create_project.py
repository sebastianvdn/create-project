import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory 



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
        settings_button.grid(row=0, column=1, sticky="WE")

        self.folder_path_entry = ttk.Entry(
            self,
            textvariable=controller.folder_path,
            state='disabled',
            width=20,
            font=("TkDefaultFont", 12)
        )
        self.folder_path_entry.grid(row=1, column=0)

        def open_folder(): 
            folder = askdirectory() 
            controller.folder_path.set(folder)
            self.folder_path_entry['textvariable']=controller.folder_path

        btn = ttk.Button(
            self,
            text='Choose Folder',
            style="Button.TButton",
            command=lambda:open_folder()
        ) 
        btn.grid(row=1, column=1)

        create_project = ttk.Button(
            self,
            text="Create Project",
            style="Button.TButton",
            cursor="hand2"  # hand1 in some systems
        )
        create_project.grid(row=2, columnspan=2, sticky="EW")


        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=12)