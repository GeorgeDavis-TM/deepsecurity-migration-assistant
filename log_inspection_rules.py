import json

from utils import Utils

class LogInspectionRules:

    srcC1WSRegion = destC1WSRegion = None
    utilsObj = None

    def __init__(self):

        self.utilsObj = Utils()

        self.srcC1WSRegion = self.utilsObj.srcC1WSRegion
        self.destC1WSRegion = self.utilsObj.destC1WSRegion

    def listLogInspectionRules(self, http, baseUrl):
        
        r = http.request('GET', baseUrl + '/loginspectionrules')

        if r.data:

            tempRules = json.loads(r.data)

            if "logInspectionRules" in tempRules:
                return tempRules["logInspectionRules"]

        else:
            print("No data returned for ", __class__.__name__)

    def migrateLogInspectionRules(self):

        srcListLogInspectionRules = self.listLogInspectionRules(self.utilsObj.httpSrc, self.utilsObj.c1wsApiEndpointBaseUrl(self.utilsObj.srcC1WSRegion))

        print(str(srcListLogInspectionRules))