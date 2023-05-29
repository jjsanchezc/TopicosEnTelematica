# Laboratorio: Map/Reduce en Python con MRJOB

## menu de siempre

## Descargar el CLI
- Primero se descarga el CLI desde la pagina de AWS 
(imagen de descarga)
- Despues se configura el aws 
(imagen de configuración)

## Crear un S3
- Existen 2 formas de hacerlo la pagina de AWS o el CLI

### AWS
(imagen)

### CLI
Para este lab se creó un s3 llamado lab-jjsanchezc-emr
```
aws s3 mb s3://lab-jjsanchezc-emr
```
***
si queremos ver que se creó correctamente podemos usar el comando 
```
aws s3 ls
```
o podemos verlo en aws como 
(imagen aws)

## Key Pairs
- Para los pares de clave se utilizará la llave creada en el lab anterior, la cual se llama "emr-key.pem"

## Creación del ClusterEMR
Para la creación del cluster se tuvo que hacer el siguente comando:
```
aws emr create-cluster \
    --release-label emr-5.26.0 \
    --service-role EMR_DefaultRole \
    --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole \
    --name emr-lab-reto-cluster \
    --applications Name=Hue Name=Spark Name=Hadoop Name=Sqoop Name=Hive \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large InstanceGroupType=TASK,InstanceCount=1,InstanceType=m4.large \
    --no-auto-terminate
```
>--release
## Creacion de configuración
Para poder crear el Cluster, primero se debe crear 

## Referencias 
https://docs.aws.amazon.com/cli/latest/reference/emr/create-cluster.html
PDF-Laboratorio-N6-Crear Cluster EMR-Hadoop
https://docs.aws.amazon.com/es_es/cli/latest/userguide/cli-services-s3-commands.html