# Laboratorio / Reto: Map/Reduce en Python con MRJOB

## menu de siempre


***
## 1. Creación ClusterEMR con CLI
## Descargar el CLI
- Primero se descarga el CLI desde la pagina de AWS 

![descarga](imagenes/descargando_CLI.png)

- Despues se configura el aws 

![config](imagenes/configurando_aws.png)

## Crear un S3
- Existen 2 formas de hacerlo la pagina de AWS o el CLI

### AWS

![createS3](imagenes/S3-desde_AWS.png)

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

![s3existentes](imagenes/existencia_s3.png)

## Key Pairs
- Para los pares de clave se utilizará la llave creada en el lab anterior, la cual se llama `"emr-key.pem"`

## Creación del ClusterEMR
Para la creación del cluster se tuvo que hacer el siguente comando:
```
aws emr create-cluster \
    --release-label emr-6.10.0 \
    --service-role EMR_DefaultRole \
    --ec2-attributes KeyName=emr-key,InstanceProfile=EMR_EC2_DefaultRole \
    --name emr-lab-reto-cluster \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large InstanceGroupType=TASK,InstanceCount=1,InstanceType=m4.large \
    --no-auto-terminate
```
`--release-label` Especifica la versión de lanzamiento de Amazon EMR <br>
`--service-role` Especifica el rol de servicio de IAM <br>
`--ec2-attributes`Configuraciones de instancias de clúster y Amazon EC2.<br>
`--name` Nombre del cluster <br>
`--applications` Aplicaciónes que se van a instalar en el cluster --applications Name=Hue Name=Spark Name=Hadoop Name=Sqoop Name=Hive \ `no se si ponerlo`<br>
`--instance-group` Especifica el numero y el tipo de instancias EC2 que se van a crear, aparte del rol que estas van a tomar, sea "MASTER", "CORE" ó "TASK" <br>

### Resultados 
- ### EC2

![cluster_ec2_res](imagenes/resultados_cluster_ec2.png)

- ### EMR

![cluster_emr_res](imagenes/resultados_cluster_emr.png)

![cluster_emr2_res](imagenes/resultados_cluster_emr2.png)

***
# 2.Conexión Main node del cluster

## conexión

para la conexion por SSH debemos usar la `"emr-key.pem"`:

cuando estemos dentro actualizaremos yum, instalamos pip, mrjob y luego git:

```
sudo yum update -y
sudo yum install git -y
sudo yum install python3-pip -y
sudo pip3 install mrjob
```

se hace la copia del repo:

```
git clone https://github.com/ST0263/st0263-2023-1.git
```

Luego de haber clonado el repo se entra en el y se realizan los siguientes comandos: 

```
cd st0263-2023-1/
cd "Laboratorio N6-MapReduce"
cd wordcount
python wordcount-local.py ../../datasets/gutenberg-small/*.txt > salida-serial.txt
```
si se hace el `sudo nano salida-serial.txt` veremos como se creó el archivo "salida-serial.txt" 
este es el resultado:

![wordcount-local](imagenes/resultado_worcount-local.png)

<br>

Ahora se quiere probar el mrjob local y se hace con el siguiente comando

```
python wordcount-mr.py ./datasets/gutenberg-small/*.txt
```

Y sus resultados deberian ser:

![wordcount-mr](imagenes/resultado_wordcount-mr.png)

![wordcount-mr](imagenes/resultado_wordcount-mr2.png)

## Referencias 
https://docs.aws.amazon.com/cli/latest/reference/emr/create-cluster.html
PDF-Laboratorio-N6-Crear Cluster EMR-Hadoop
https://docs.aws.amazon.com/es_es/cli/latest/userguide/cli-services-s3-commands.html
