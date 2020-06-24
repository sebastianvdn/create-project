from github import Github, GithubException
import os, subprocess
from pathlib import Path

class CreateProject:
    def __init__(
        self, repo_name, dir_path, github_full_name=None,
        venv_name="venv", token="8a8826a6119af94f7e1f9bd63906a6d2ecd9ccca"
        ):
        self.token = token
        self.repo_name = repo_name
        self.dir_path = Path(dir_path)
        self.full_path = os.path.join(dir_path, repo_name)
        self.github_full_name = github_full_name
        self.venv_name = venv_name

    def init_local_git(self):
        os.mkdir(self.full_path)
        os.chdir(self.full_path)
        # os.system(f'echo # {self.repo_name} >> README.md')
        subprocess.run(["echo", '#', self.repo_name, '>>', "README.md"],shell=True)
        subprocess.run(['git', 'init'])
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', "First commit"])

    def create_github_repo(self):        
        g = Github(self.token)
        user = g.get_user()
        try:
            repo = user.create_repo(self.repo_name)
            self.github_full_name = repo.full_name
        except GithubException as e:
            print(e)

    def upload_files_to_github(self):
        os.chdir(self.full_path)
        subprocess.run(
            ["git", "remote", "add", "origin", f'https://github.com/{self.github_full_name}.git']
        )
        subprocess.run(['git', 'push', '-u', 'origin', 'master'])

    def create_env(self):
        os.chdir(self.full_path)
        subprocess.run(['python', '-m', 'venv', self.venv_name])



repo_name = input("Give up the name that you want to use for you repo: ")
dir_path = input("Give up the directory path you want the rope to be created in: ")
create_env = input("Do you want a python environment to be created? (y/n): ")
while create_env.lower() not in ('y', 'n'):
    print("Looks like you didn't use y/n. Try again")
    create_env = input("Create python environment? (y/n): ")


project = CreateProject(repo_name, dir_path)
project.create_github_repo()
project.init_local_git()
project.upload_files_to_github()
if create_env == "y":
    project.create_env()

print("Done, your project is created.")