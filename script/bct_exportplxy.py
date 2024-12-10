import traceback
from pyrx_imp import Rx, Ge, Gi, Db, Ap, Ed, Cv
    
import math
import pandas as pd
    
# https://www.theswamp.org/index.php?topic=59425.0
        
def py_samplepolylinexy() -> None:
    try:
        es = Ed.Editor.entSel("\nPick polyline for sampling: ", Db.Polyline.desc())
        if es[0] != Ed.PromptStatus.eNormal:
            raise Exception ("Dude, you missed!", es)
        pl = Db.Polyline(es[1])
        curve = pl.getAcGeCurve()
    
        # get distance as positive float
        while True:
            ssResult = Ed.Editor.getDouble("\nEnter distance interval:")
            if ssResult[0] == Ed.PromptStatus.eNormal : 
                if ssResult[1] > 0 :
                    break
                print("\nEnter a positive value")
        distint = ssResult[1]
        nspts = math.floor(pl.getDistAtParam(pl.getEndParam())/distint)
        spts = curve.getSamplePoints(nspts)
        
        # shift points to list
        xyTable = {
            "X": [],
            "Y": [],
        }
        for pt in spts[0]:
            xyTable["X"].append(pt.x)
            xyTable["Y"].append(pt.y)
    
        # get filename for storing and export
        path = Ed.Core.getFileD("Enter file name for storing xy data table", "myxyfile.csv", "cs", 32)
        df = pd.DataFrame(xyTable)
        df.to_csv(path, index = False, sep=';')
    
    except Exception as err:
        traceback.print_exception(err)