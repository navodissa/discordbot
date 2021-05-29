import jsonHandler as jshand
import json


class UserAuth():

    def authenticate(self):
        header_keys = ['ver', 'msgGrp', 'msgTyp',
                       'chnlId', 'clVer', 'usrId', 'sesnId']
        header_vals = ["DFN_JSON_1.0", 5, 1, 22,
                       "DFNUAWEB_SMB_X_1.001.00.781+324068b8", "", ""]

        DAT_keys = ['lgnNme', 'pwd']
        DAT_vals = ['893000033', 'cc03fea63e5aa3438ca0db0127bf49da']

        # Call jsonbuilder functions to build the requested json
        json_head = jshand.buildJSON(header_keys, header_vals)
        json_DAT = jshand.buildJSON(DAT_keys, DAT_vals)
        jsonVal = {"HED": json_head, "DAT": json_DAT}

        return jsonVal

    def setAuthValues(self, response):
        response = json.loads(response)
        head_values = response["HED"]
        self.sesnId = head_values["sesnId"]
        self.hedUsrId = head_values["usrId"]
        self.clVer = head_values["clVer"]

        dat_values = response["DAT"]
        self.datUsrId = dat_values["usrId"]

    # Setting up the getters

    def getSesnId(self):
        return self.sesnId

    def getHedUsrId(self):
        return self.hedUsrId

    def getClVer(self):
        return self.clVer

    def getDatUsrId(self):
        return self.datUsrId
