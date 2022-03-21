# Deep Security Migration Assistant

This project is still in development, built for the migration between Trend Micro Cloud One tenants. For more information on the migration, please refer to the product documentation [here](https://cloudone.trendmicro.com/docs/workload-security/api-reference/tag/Common-Object-Import-Tasks).

## Usage

### Deployment

In order to deploy the example, you need to run the following command:

```
$ serverless deploy -s dev
```

After running deploy, you should see output similar to:

```bash
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
........
Serverless: Stack create finished...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service aws-python.zip file to S3 (711.23 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
.................................
Serverless: Stack update finished...
Service Information
service: aws-python
stage: dev
region: us-east-1
stack: aws-python-dev
resources: 6
functions:
  api: aws-python-dev-hello
layers:
  None
```

After successful deployment, you can see the stack on AWS CloudFormation.

## Configuration

All configurable options are found in the serverless.yml file under `.custom`

| Fields | Description | Required? |
|--------| ----------- | --------- |
|`awscli_profile` | AWS CLI profile to use to deploy the Serverless CloudFormation stack | Yes |
| `aws_region` | AWS Region to deploy the CloudFormation stack to | Yes |
| `srcC1WSApiKey` | Cloud One API key of the source Cloud One tenant  | Yes |
| `destC1WSApiKey` | Cloud One API key of the destination Cloud One tenant | Yes |
| `exceptionPolicies` | Policies that need to be exempted from the migration | Yes |