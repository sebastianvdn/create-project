import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import askdirectory 
import os
from github import Github, GithubException



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
            font=("TkDefaultFont", 14)
        )
        self.folder_path_entry.grid(row=1, column=0)

        def open_folder(): 
            folder = askdirectory() 
            controller.folder_path.set(folder)
            self.folder_path_entry['textvariable'] = controller.folder_path

        self.full_path = os.path.join(controller.folder_path, controller.project_name.get())
        self.github_full_name = None

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
            cursor="hand2"  # hand1 in some systems,
            command=lambda : [self.create_github_repo(), self.init_local_git(), self.upload_files_to_github(), self.create_venv()]
        )
        create_project.grid(row=2, columnspan=2, sticky="EW")


        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=12)

    def init_local_git(self):
        """
        initialize local git repo
        """
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
        except GithubException as e:
            messagebox.showerror(
                'Github error', f"""
                The following error was thrown by the gitub api: {e}.
                There are mainly two reasons, the project name is not available or 
                you api token is not valid. For the second one chekout
                https://docs.cachethq.io/docs/github-oauth-token#:~:text=Generate%20a%20new%20token,list%20of%20tokens%20from%20before.
                """
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
            os.system(f"python -m venv {self.venv_name}")
