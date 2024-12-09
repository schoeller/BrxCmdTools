import os
from dulwich import porcelain

# Constants
REPO_NAME = "BrxCmdTools"
REPO_URL = "https://github.com/schoeller/BrxCmdTools.git"

def str_find(file, string):
    """Checks if a string is present in a file."""
    with open(file, 'r', encoding='utf-8') as target_file:
        for line in target_file:
            if string in line:
                return True
    return False

def initonload():
    """Initializes the configuration on load."""
    try:
        initstring = (
            "from pyrx_imp import Rx, Ge, Gi, Db, Ap, Ed\n\n"
            "def OnPyLoadDwg() -> None:\n"
            f"    Ap.Application.loadPythonModule(\"{os.path.join(os.getenv('APPDATA'), REPO_NAME, 'commands.py')}\")\n"
            "    print('Loading BrxCmdTools')"
        )
        fname = os.path.join(os.getenv('LOCALAPPDATA'), "Programs", "PyRx", "Bin", "pyrx_onload.py")
        print(fname)

        if not os.path.exists(fname):
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(initstring.replace("\\", "/") + '\n')
                print("Configuration file created.")
        elif str_find(fname, REPO_NAME):
            print("Configuration already exists.")
        else:
            with open(fname, 'a', encoding='utf-8') as f:
                f.write(initstring.replace("\\", "/") + '\n')
                print("Configuration extended.")
    except Exception as e:
        print(f"Could not initialize: {e}")

if __name__ == "__main__":
    appdata_path = os.getenv('APPDATA')
    repo_dir = os.path.join(appdata_path, REPO_NAME)

    try:
        if os.path.exists(repo_dir):
            print(f"The directory {repo_dir} already exists.")
        else:
            porcelain.clone(REPO_URL, repo_dir)
            print(f"Repository successfully cloned to {repo_dir}.")
    except Exception as e:
        print(f"Error while cloning repository: {e}")

    initonload()
