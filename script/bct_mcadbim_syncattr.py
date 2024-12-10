def mcadbim_attsync():
    try:
        # Translation table
        translation_table = {
            "DIN EN 558 Flanged Angle Valve": "eBimFlowController",
            "DIN 2605 Elbow Type 10 45 Deg": "eBimFlowSegment",
            # add more translation pairs to table
        }
    
        # Suchbedingungen
        bimTypeKey = "Component name~MCAD"
    
        print(f"Looking up objects with TypeKey {bimTypeKey}")
        print("Using translation table")
        print(translation_table)
    
        db = Db.curDb()
        ids = db.objectIds(Db.BlockReference.desc())
    
        for id in ids:
            props = set(Brx.DbProperties.listAll(id))
            if bimTypeKey in props and Brx.DbProperties.isValid(id, bimTypeKey)[0]:
                acval = Brx.DbProperties.getValue(id, bimTypeKey)
                if acval.format() in translation_table:
                    bimElementTypeStr = translation_table[acval.format()]
                    bimElementType = getattr(Bim.BimElementType, bimElementTypeStr)
                    print(f"ID: {id}, Current Classification: {Bim.BimClassification.getClassification(id)}")
                    if Bim.BimClassification.getClassification(id) != bimElementType:
                        Bim.BimClassification.classifyAs(id, bimElementType)
                        print(f"ID: {id} classified as {bimElementTypeStr}")
    
    except Exception as err:
        traceback.print_exception(err)