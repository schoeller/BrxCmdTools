import traceback
from pyrx_imp import Ap, Db, Ed, Ge, Gi, Gs, Rx, Bim

from helper import helper
from helper import repo

print("added command - bct_test")
print("added command - bct_reloadmodules")
print("added command - bct_repoupdate")

# On PYRELOAD reload all used custom modules
def OnPyReload() -> None:
    try:
        import importlib
        importlib.reload(helper)
        importlib.reload(repo)
        print("\nReloading all modules")
    except Exception as err:
        print(err)

def PyRxCmd_bct_test():
    try:
        print("roks")
    except Exception as err:
        print(err)

def PyRxCmd_bct_reloadcommands():
    try:
        helper.reload_commands()
        print("#TODO: initialize OnPyReload on commands")
    except Exception as err:
        print(err)

def PyRxCmd_bct_repoupdate():
    try:
        repo.pull_git_changes()
    except Exception as err:
        print(err)
