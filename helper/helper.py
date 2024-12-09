import traceback
from pyrx_imp import Ap, Db, Ed, Ge, Gi, Gs, Rx, Bim
import repo

def reload_commands():
    try:
        print(repo.get_repo_dir())

    except Exception as e:
        print(f"Error displaying changes: {e}")
