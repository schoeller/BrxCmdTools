import os
from dulwich import porcelain

REPO_NAME = "BrxCmdTools"
REPO_URL = "https://github.com/schoeller/BrxCmdTools.git"

def get_repo_dir():
    return os.path.join(os.getenv('APPDATA'), REPO_NAME)

def show_git_changes():
    repo_dir = get_repo_dir()
    try:
        if not os.path.exists(repo_dir):
            porcelain.clone(REPO_URL, repo_dir)
            print(f"Repository successfully cloned to {repo_dir}.")

        # TODO: make me work

    except Exception as e:
        print(f"Error displaying changes: {e}")

def pull_git_changes():
    repo_dir = get_repo_dir()
    try:
        if not os.path.exists(repo_dir):
            porcelain.clone(REPO_URL, repo_dir)
            print(f"Repository successfully cloned to {repo_dir}.")
        else:
            porcelain.pull(repo_dir)
            print(f"Repository successfully pulled to {repo_dir}.")
    except Exception as e:
        print(f"Error displaying changes: {e}")

if __name__ == "__main__":
    show_git_changes()
    pull_git_changes()
