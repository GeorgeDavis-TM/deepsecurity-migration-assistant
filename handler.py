import json
import logging

from policies import Policies
from log_inspection_rules import LogInspectionRules
from integrity_monitoring_rules import IntegrityMonitoringRules
from firewall_rules import FirewallRules
from application_control_rules import ApplicatonControlRules
# from utils import Utils

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def main(event, context):

    policiesObj = Policies()
    policiesObj.migratePolicy()

    logInspectionRulesObj = LogInspectionRules()    
    logInspectionRulesObj.migrateLogInspectionRules()

    integrityMonitoringRulesObj = IntegrityMonitoringRules()    
    integrityMonitoringRulesObj.migrateIntegrityMonitoringRules()

    firewallRulesObj = FirewallRules()    
    firewallRulesObj.migrateFirewallRules()

    applicatonControlRulesObj = ApplicatonControlRules()    
    applicatonControlRulesObj.migrateApplicatonControlRules()

    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
