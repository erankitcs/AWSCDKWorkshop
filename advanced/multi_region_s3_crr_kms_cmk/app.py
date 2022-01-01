#!/usr/bin/env python3
from aws_cdk import core as cdk
from lib.multi_region_s3_crr_kms_cmk_source_stack import MultiRegionS3CrrKmsCmkSourceStack
from lib.multi_region_s3_crr_kms_cmk_target_stack import MultiRegionS3CrrKmsCmkTargetStack
from multi_region_s3_crr_kms_cmk_source import MultiRegionS3CrrKmsCmkSourceProps


account_id = '<YOUR ACCOUNT ID>'
env_target=cdk.Environment(account=account_id, region='us-east-2') 
env_source=cdk.Environment(account=account_id, region='us-east-1')
#env_target=cdk.Environment(region='us-east-2') 
#env_source=cdk.Environment(region='us-east-1')

app = cdk.App()

target_stack = MultiRegionS3CrrKmsCmkTargetStack(app, 'MultiRegionS3CrrKmsCmkTarget', env=env_target)

source_props = MultiRegionS3CrrKmsCmkSourceProps(
    target_bucket=target_stack.target_bucket,
    target_key_id_ssm_parameter_name=target_stack.target_key_id_ssm_parameter_name,
    target_region=target_stack.region
)

source_stack = MultiRegionS3CrrKmsCmkSourceStack(app, 'MultiRegionS3CrrKmsCmkSource',
    env=env_source,
    props=source_props
)

source_stack.add_dependency(target_stack)

app.synth()
