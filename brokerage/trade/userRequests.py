import authentication as auth
import jsonHandler as jshand


def getCustomerDetails(obj):
    header_keys = ['ver', 'msgGrp', 'msgTyp',
                   'chnlId', 'clVer', 'usrId', 'sesnId']
    header_vals = ["DFN_JSON_1.0", 10, 3, 22,
                   "DFNUAWEB_SMB_X_1.001.00.781+324068b8", obj.getDatUsrId(), obj.getSesnId()]

    DAT_keys = ['cusId']
    DAT_vals = [obj.getDatUsrId()]

    # Call jsonbuilder functions to build the requested json
    json_head = jshand.buildJSON(header_keys, header_vals)
    json_DAT = jshand.buildJSON(DAT_keys, DAT_vals)
    jsonVal = {"HED": json_head, "DAT": json_DAT}

    return jsonVal
