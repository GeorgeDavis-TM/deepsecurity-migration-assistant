import json

from utils import Utils

class Policies:

    srcC1WSRegion = destC1WSRegion = None
    utilsObj = None

    def __init__(self):

        self.utilsObj = Utils()

        self.srcC1WSRegion = self.utilsObj.srcC1WSRegion
        self.destC1WSRegion = self.utilsObj.destC1WSRegion

    def listPolicies(self, http, baseUrl):

        r = http.request('GET', baseUrl + '/policies')

        tempPolicies = json.loads(r.data)

        if "policies" in tempPolicies:

            return tempPolicies["policies"]

    def buildPolicyHierarchy(self, srcPolicies):

        hierarchyDict = {}    

        for srcPolicy in srcPolicies:

            # parent policy
            if "parentID" not in srcPolicy:
                hierarchyDict.update({srcPolicy["ID"]: []})

            # child policy
            else:
                if srcPolicy["parentID"] not in hierarchyDict:
                    hierarchyDict.update({srcPolicy["parentID"]: []})        
                tempHierarchyList = hierarchyDict[srcPolicy["parentID"]]
                tempHierarchyList.append(srcPolicy["ID"])
                hierarchyDict.update({srcPolicy["parentID"]: tempHierarchyList})    

        return hierarchyDict

    def cleanupPolicy(self, policy):

        print(str(policy))
        pass

    def copyPolicy(self, httpDest, policy):

        pass

    def migratePolicy(self):        

        srcListPolicies = self.listPolicies(self.utilsObj.httpSrc, self.utilsObj.c1wsApiEndpointBaseUrl(self.utilsObj.srcC1WSRegion))
        destListPolicies = self.listPolicies(self.utilsObj.httpDest, self.utilsObj.c1wsApiEndpointBaseUrl(self.utilsObj.destC1WSRegion))

        hierarchyDict = self.buildPolicyHierarchy(srcListPolicies)

        renameList = []
        migrateList = []

        for srcPolicy in srcListPolicies:
            for destPolicy in destListPolicies:
                if srcPolicy["name"] == destPolicy["name"]:
                    renameList.append(srcPolicy["name"])
                
        for srcPolicy in srcListPolicies:
            if srcPolicy["name"] not in renameList:            
                migrateList.append(srcPolicy["name"])

        print("Rename List -", str(renameList))

        print("Migrate List -", str(migrateList))

        print("Hierarchy List - ", str(hierarchyDict))

        # for srcPolicy in srcListPolicies:

        #     if srcPolicy["name"] in migrateList:

        #         copyPolicy(httpDest, cleanupPolicy(srcPolicy))