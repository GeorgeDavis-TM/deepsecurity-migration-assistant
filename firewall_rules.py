import json

from utils import Utils

class FirewallRules:

    srcC1WSRegion = destC1WSRegion = None
    utilsObj = None

    def __init__(self):

        self.utilsObj = Utils()

        self.srcC1WSRegion = self.utilsObj.srcC1WSRegion
        self.destC1WSRegion = self.utilsObj.destC1WSRegion

    def listFirewallRules(self, http, baseUrl):
        
        r = http.request('GET', baseUrl + '/firewallrules')

        if r.data:

            tempRules = json.loads(r.data)

            if "firewallRules" in tempRules:
                return tempRules["firewallRules"]

        else:
            print("No data returned for ", __class__.__name__)

    def migrateFirewallRules(self):

        srcListFirewallRules = self.listFirewallRules(self.utilsObj.httpSrc, self.utilsObj.c1wsApiEndpointBaseUrl(self.utilsObj.srcC1WSRegion))

        print(str(srcListFirewallRules))