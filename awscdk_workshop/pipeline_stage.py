from aws_cdk import (
    core
)
from .awscdk_workshop_stack import AwscdkWorkshopStack

class WorkshopPipelineStage(core.Stage):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        service = AwscdkWorkshopStack(self, 'WebService')