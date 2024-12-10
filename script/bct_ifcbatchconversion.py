import traceback
from pyrx_imp import Rx, Ge, Gs, Gi, Db, Ap, Ed, Bim
    
import wx
import os, pathlib
    
def openSaveIfcSideDrawing(path, opts):
    print("\nProcessing {} ".format(path))
    db = Db.Database(True, False)
    Bim.IfcImportOptions.importIfcFile(db, path, opts)
    path = str(path[:-3]) + "dwg"
    db.saveAs(path)
    print("\nSaved to {} ".format(path))
    db.closeInput(True)
            
def brxIfcConvert():
    try:
        ifcext = ".ifc".casefold()
        opts = Bim.IfcImportOptions()
    
        dlg = wx.DirDialog(None, "Choose input directory","",
                wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
    
        if dlg.ShowModal() != wx.ID_OK:
            print("You Cancelled The Dialog!")
            return
    
        for fname in next(os.walk(dlg.GetPath()), (None, None, []))[2]:
            ext = pathlib.Path(fname).suffix.casefold()
            if ext != ifcext:
                continue
            fpath = '{}\\{}'.format(dlg.GetPath(),fname)
            openSaveIfcSideDrawing(fpath, opts)
            
    except Exception as err:
        traceback.print_exception(err)