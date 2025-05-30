### CloudFormation para crear un repositorio en Amazon ECR con políticas de limpieza automática:

aws cloudformation deploy \
  --template-file ecr_repository_template.yml \
  --stack-name ml-model-ecr \
  --capabilities CAPABILITY_NAMED_IAM



plantilla de AWS CloudFormation para crear un proyecto de CodeBuild que:

Clona tu repo de GitHub

Usa Docker en modo privilegiado

Construye y sube una imagen a ECR

Guarda artefactos en S3


aws cloudformation deploy \
  --template-file codebuild_project_template.yml \
  --stack-name codebuild-ml-model-stack \
  --parameter-overrides ArtifactBucket=tu-bucket CodeRepo=https://github.com/tuusuario/tu-repo.git BranchName=main \
  --capabilities CAPABILITY_NAMED_IAM



# permisos IAM:

Agregar permisos manualmente desde la consola
Ve a IAM > Roles en la consola de AWS.

Busca el rol asociado a CodeBuild, por ejemplo:
MyCodeBuildRole 

Haz clic en "Agregar permisos" > "Adjuntar políticas".

Busca y selecciona:

AmazonEC2ContainerRegistryPowerUser

Guarda.


