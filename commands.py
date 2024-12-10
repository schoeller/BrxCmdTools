import traceback
from pyrx_imp import Ap, Db, Ed, Ge, Gi, Gs, Rx, Bim

from helper import helper
from helper import repo
from script import bct_create_bfr_symbol_styles
from script import bct_mcadbim_syncattr
from script import bct_ifcbatchconversion
from script import bct_exportplxy
from script import bct_layerimportexport
from script import bct_osmtin

print("added command - bct_reloadcommands")
print("added command - bct_repodiffs")
print("added command - bct_repoupdate")
print("added command - bct_bfrsymbolstyles")
print("added command - bct_mcadbim_syncattr")
print("added command - bct_ifcbatchconversion")
print("added command - bct_exportplxy")
print("added command - bct_layerimport")
print("added command - bct_layerexport")
print("added command - bct_getosmtin")

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

def PyRxCmd_bct_mcadbim_attsync():
    try:
        bct_mcadbim_syncattr.mcadbim_attsync()
    except Exception as err:
        print(err)

def PyRxCmd_bct_ifcbatchconversion():
    try:
        bct_ifcbatchconversion.brxIfcConvert()
    except Exception as err:
        print(err)

def PyRxCmd_bct_ifcbatchconversion():
    try:
        bct_exportplxy.py_samplepolylinexy()
    except Exception as err:
        print(err)

def PyRxCmd_bct_layerimport():
    try:
        bct_layerimportexport.py_layerimport()
    except Exception as err:
        print(err)

def PyRxCmd_bct_layerexport():
    try:
        bct_layerimportexport.py_layerexport()
    except Exception as err:
        print(err)

def PyRxCmd_bct_osm4tin():
    try:
        bct_osmtin.cvgetosmtin()
    except Exception as err:
        print(err)

cvgetosmtin