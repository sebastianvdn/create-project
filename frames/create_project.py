import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import askdirectory 
import os
from github import Github, GithubException
import time
from multiprocessing import Pool


# Create two pools
pool = Pool(processes=2)


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

        check_btn = ttk.Checkbutton(
            self,
            text="  Create Virtual Env",
            style="LightText.TCheckbutton",
            variable=controller.create_venv,
        )
        check_btn.grid(row=0, column=0)

        project_name_label = ttk.Label(
            self,
            text="Project name:",
            style="LightText.TLabel"
        )
        project_name_label.grid(column=0, row=1)

        project_name_entry = tk.Entry(
            self,
            textvariable=controller.project_name,
            font=("TkDefaultFont", 14)
        )
        project_name_entry.grid(column=1, row=1, sticky="EW")


        self.folder_path_entry = ttk.Entry(
            self,
            textvariable=controller.folder_path,
            state='disabled',
            font=("TkDefaultFont", 14)
        )
        self.folder_path_entry.grid(row=2, column=0)

        def open_folder(): 
            folder = askdirectory() 
            controller.folder_path.set(folder)
            self.folder_path_entry['textvariable'] = controller.folder_path
        self.github_full_name = None
        self.full_path = None
        btn = ttk.Button(
            self,
            text='Choose Folder',
            style="Button.TButton",
            command=lambda:open_folder()
        ) 
        btn.grid(row=2, column=1, sticky="EW")

        progbar = ttk.Progressbar(
            self,
            orient=tk.HORIZONTAL, 
            mode='determinate',
            length=200,
            maximum=4,
            variable=controller.progress_int_var,
            style="TProgressbar"
        )
        progbar.grid(row=3, columnspan=2, sticky="EW")

        create_project = ttk.Button(
            self,
            text="Create Project",
            style="Button.TButton",
            cursor="hand2",  # hand1 in some systems,
            command=lambda:  self.create_github_repo(),
        )
        create_project.grid(row=4, columnspan=2, sticky="EW")


        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=12)

    def init_local_git(self):
        """
        initialize local git repo
        """
        self.full_path = os.path.join(self.controller.folder_path.get(), self.controller.project_name.get())
        os.mkdir(self.full_path)
        os.chdir(self.full_path)
        os.system(f'echo # {self.controller.project_name.get()} >> README.md')
        os.system("git init")
        os.system("git add .")
        os.system('git commit -m "First commit"')

    def create_github_repo(self):
        """Create repo on github"""        
        g = Github(self.controller.github_api_token.get())
        user = g.get_user()
        try:
            repo = user.create_repo(self.controller.project_name.get())
            self.github_full_name = repo.full_name
            # Create local folder
            self.add1()
            print(self.controller.progress_int_var.get())
            self.init_local_git()
            self.add1()
            print(self.controller.progress_int_var.get())
            self.upload_files_to_github()
            self.add1()
            print(self.controller.progress_int_var.get())
            self.create_venv()
            self.add1()
            print(self.controller.progress_int_var.get())
        except GithubException as e:
            messagebox.showerror(
                'Github error', e.data["message"] + ".\nMake sure you are using a valid "+
                "API token and the project name is still available."
            )

    def upload_files_to_github(self):
        """Upload files to github"""
        os.chdir(self.full_path)
        os.system(f'git remote add origin https://github.com/{self.github_full_name}.git')
        os.system('git push -u origin master')

    def create_venv(self):
        """Create venv"""
        if self.controller.create_venv.get():
            os.chdir(self.full_path)
            os.system(f"python -m venv {self.controller.default_venv_name.get()}")

    def add1(self):
        print(11111111111111111111111111111111111111)
        if self.controller.progress_int_var.get() == 4:
            self.controller.progress_int_var.set(0)
            print(2222222222222222222222222222222222222222222222222222)
        else:
            self.controller.progress_int_var.set(self.controller.progress_int_var.get()+1)
            print(333333333333333333333333333333333333333333333333)