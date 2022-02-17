import os
import json
import urllib3

class Utils:

    srcC1WSRegion = destC1WSRegion = None
    httpSrc = httpDest = None
    httpSrcHeaders = httpDestHeaders = {}

    def __init__(self):

        self.srcC1WSApiKey = str(os.environ.get("srcC1WSApiKey"))
        self.destC1WSApiKey = str(os.environ.get("destC1WSApiKey"))

        self.httpSrcHeaders = {
            'Content-Type': 'application/json',
            'Authorization': 'ApiKey ' + str(self.srcC1WSApiKey),
            'api-version': 'v1'
        }

        self.httpDestHeaders = {
            'Content-Type': 'application/json',
            'Authorization': 'ApiKey ' + str(self.destC1WSApiKey),
            'api-version': 'v1'
        }

        self.httpSrc = urllib3.PoolManager(headers=self.httpSrcHeaders)
        self.httpDest = urllib3.PoolManager(headers=self.httpDestHeaders)

        self.srcC1WSRegion = self.getApiKeyRegion(self.httpSrc, self.srcC1WSApiKey)
        self.destC1WSRegion = self.getApiKeyRegion(self.httpDest, self.destC1WSApiKey)

        print("Migrating from", self.srcC1WSRegion, "to", self.destC1WSRegion)

    def c1AccountsApiEndpointBaseUrl(self):

        return "https://accounts.cloudone.trendmicro.com/api"

    # Returns Cloud One region-based Services API Endpoint URL.
    def c1wsApiEndpointBaseUrl(self, c1TrendRegion):
        
        return "https://workload." + str(c1TrendRegion) + ".cloudone.trendmicro.com/api"

    # Retrieve API Key ID from the raw API Key passed to this function.
    def parseApiKeyForKeyId(self, rawApiKey):

        return rawApiKey.split(':')[0]

    def getApiKeyRegion(self, http, apiKeyId):    

        r = http.request('GET', self.c1AccountsApiEndpointBaseUrl() + '/apikeys/' + self.parseApiKeyForKeyId(apiKeyId))

        return json.loads(r.data)["urn"].split(":")[3]
