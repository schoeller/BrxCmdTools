import traceback
from pyrx_imp import Ap, Db, Ed, Ge, Gi, Gs, Rx, Bim

from helper import helper

print("added command - test")

# On PYRELOAD reload all used custom modules
def OnPyReload() -> None:
    try:
        import importlib
        importlib.reload(helper)
        print("\nReloading all modules")
    except Exception as err:
        print(err)

# define a command
def PyRxCmd_bct_test():
    try:
        print("roks")
    except Exception as err:
        print(err)

def PyRxCmd_bct_reloadmodules():
    try:
        #TODO: initialize OnPyReload on commands
    except Exception as err:
        print(err)