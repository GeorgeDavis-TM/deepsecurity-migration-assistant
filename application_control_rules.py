import json

from utils import Utils

class ApplicatonControlRules:

    srcC1WSRegion = destC1WSRegion = None
    utilsObj = None

    def __init__(self):

        self.utilsObj = Utils()

        self.srcC1WSRegion = self.utilsObj.srcC1WSRegion
        self.destC1WSRegion = self.utilsObj.destC1WSRegion

    def listApplicatonControlRules(self, http, baseUrl):
        
        r = http.request('GET', baseUrl + '/applicationcontrolglobalrules')

        if r.data:

            tempRules = json.loads(r.data)

            if "applicationControlGlobalRules" in tempRules:
                return tempRules["applicationControlGlobalRules"]
        
        else:
            print("No data returned for ", __class__.__name__)

    def migrateApplicatonControlRules(self):

        srcListApplicatonControlRules = self.listApplicatonControlRules(self.utilsObj.httpSrc, self.utilsObj.c1wsApiEndpointBaseUrl(self.utilsObj.srcC1WSRegion))

        print(str(srcListApplicatonControlRules))