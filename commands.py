import traceback
from pyrx_imp import Ap, Db, Ed, Ge, Gi, Gs, Rx, Bim

from helper import helper
from helper import repo
from script import bct_create_bfr_symbol_styles

print("added command - bct_reloadcommands")
print("added command - bct_repodiffs")
print("added command - bct_repoupdate")
print("added command - bct_bfrsymbolstyles")

def OnPyReload() -> None:
    try:
        import importlib
        importlib.reload(helper)
        importlib.reload(repo)
        print("\nReloading all modules")
    except Exception as err:
        print(err)

def PyRxCmd_bct_reloadcommands():
    try:
        helper.reload_commands()
        print("#TODO: initialize OnPyReload on commands")
    except Exception as err:
        print(err)

def PyRxCmd_bct_repodiffs():
    try:
        repo.check_for_updates()
    except Exception as err:
        print(err)

def PyRxCmd_bct_repoupdate():
    try:
        repo.pull_git_changes()
    except Exception as err:
        print(err)

def PyRxCmd_bct_bfrsymbolstyles():
    try:
        bct_create_bfr_symbol_styles.cv_create_bfr_symbol_styles()
    except Exception as err:
        print(err)