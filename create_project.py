from github import Github
import os

class CreateProject:
    def __init__(self, repo_name, dir_path, github_full_name=None, token="051920f87749d7021df0fd5543998d22b37a9680"):
        self.token = token
        self.repo_name = repo_name
        self.dir_path = dir_path
        self.github_full_name = github_full_name

    def init_local_git(self):
        os.mkdir(os.path.join(self.dir_path, self.repo_name))
        os.chdir(os.path.join(self.dir_path, self.repo_name))
        os.system(f'echo # {self.repo_name} >> README.md')
        os.system("git init")
        os.system("git add .")
        os.system('git commit -m "First commit"')

    def create_github_repo(self):        
        g = Github(self.token)
        user = g.get_user()
        repo = user.create_repo(self.repo_name)
        self.github_full_name = repo.full_name

    def upload_files_to_github(self):
        os.chdir(os.path.join(self.dir_path, self.repo_name))
        os.system(f'git remote add origin https://github.com/{self.github_full_name}.git')
        os.system('git push -u origin master')


repo_name = input("Give up the name that you want to use for you repo: ")
dir_path = input("Give up the directory path you want the rope to be created in: ")
create_env = input("Do you want a python environment to be created? (y/n)")
while create_env.lower() != "y" or create_env.lower() != "n":
    print("Looks like you didn't use y/n. Try again")
    create_env = input("Create python environment? (y/n)")


project = CreateProject(repo_name, dir_path)
project.init_local_git()
project.create_github_repo()
project.upload_files_to_github()
print("Done, your project is created.")