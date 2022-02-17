import json

from utils import Utils

class IntegrityMonitoringRules:

    srcC1WSRegion = destC1WSRegion = None
    utilsObj = None

    def __init__(self):

        self.utilsObj = Utils()

        self.srcC1WSRegion = self.utilsObj.srcC1WSRegion
        self.destC1WSRegion = self.utilsObj.destC1WSRegion

    def listIntegrityMonitoringRules(self, http, baseUrl):
        
        r = http.request('GET', baseUrl + '/integritymonitoringrules')

        if r.data:

            tempRules = json.loads(r.data)

            if "integrityMonitoringRules" in tempRules:
                return tempRules["integrityMonitoringRules"]

        else:
            print("No data returned for ", __class__.__name__)

    def migrateIntegrityMonitoringRules(self):

        srcListIntegrityMonitoringRules = self.listIntegrityMonitoringRules(self.utilsObj.httpSrc, self.utilsObj.c1wsApiEndpointBaseUrl(self.utilsObj.srcC1WSRegion))

        print(str(srcListIntegrityMonitoringRules))