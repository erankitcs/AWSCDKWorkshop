from aws_cdk import core as cdk
from aws_cdk import aws_s3 as s3
from multi_region_s3_crr_kms_cmk_source import (
    MultiRegionS3CrrKmsCmkSource,
    MultiRegionS3CrrKmsCmkSourceProps
)


class MultiRegionS3CrrKmsCmkSourceStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str,
                 props: MultiRegionS3CrrKmsCmkSourceProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        _props = MultiRegionS3CrrKmsCmkSourceProps(
            target_bucket=props.target_bucket,
            target_key_id_ssm_parameter_name=props.target_key_id_ssm_parameter_name,
            target_region=props.target_region
            )
            
        _my_target_construct = MultiRegionS3CrrKmsCmkSource(self, 'MySource', _props)
