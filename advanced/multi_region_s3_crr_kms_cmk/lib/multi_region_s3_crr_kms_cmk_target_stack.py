from aws_cdk import core as cdk
from aws_cdk import aws_s3 as s3
from multi_region_s3_crr_kms_cmk_target import MultiRegionS3CrrKmsCmkTarget


class MultiRegionS3CrrKmsCmkTargetStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self._my_target_construct = MultiRegionS3CrrKmsCmkTarget(self, 'MyTarget')
        
    @property
    def target_bucket(self):
        return self._my_target_construct.target_bucket
        
    @property
    def target_key_id_ssm_parameter_name(self):
        return self._my_target_construct.target_key_id_ssm_parameter_name
        
