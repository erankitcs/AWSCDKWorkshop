from aws_cdk import (
    core,
    aws_codecommit as codecommit,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    pipelines as pipelines
)
from .pipeline_stage import WorkshopPipelineStage

class WorkshopPipelineStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Pipeline code will go here
        # Creates a CodeCommit repository called 'WorkshopRepo'
        repo = codecommit.Repository(
            self, 'WorkshopRepo',
            repository_name= "WorkshopRepo"
        )

        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()

        pipeline = pipelines.CdkPipeline(
            self, 'CDKWorkshopPipeline',
            cloud_assembly_artifact = cloud_assembly_artifact,

            ### Generate source artifact from repository.
            source_action = codepipeline_actions.CodeCommitSourceAction(
                action_name = 'CodeCommit', ##  Any GIT bash source here.
                output = source_artifact, ## where artifact is stored
                repository = repo ## repo to draw the code.
            ),
            ## Build Source code into Cloud Assembly artifact.
            synth_action = pipelines.SimpleSynthAction(
                install_commands = [
                    'npm install -g aws-cdk',
                    'pip install -r requirements.txt'
                ],
                synth_command ='npx cdk synth',
                source_artifact=source_artifact,
                cloud_assembly_artifact= cloud_assembly_artifact
            )
        )
        deploy = WorkshopPipelineStage(self, 'Deploy')
        pipeline.add_application_stage(deploy)