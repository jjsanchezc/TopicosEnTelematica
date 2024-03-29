# Laboratorio / Reto: Map/Reduce en Python con MRJOB

**Tabla de Contenido**

1. [Laboratorio Parte1](#lab1)
2. [Laboratorio Parte2](#lab2)
4. [Reto de programación en Map/Reduce](RetoProgramacion/README.md)
5. [Referencias](#ref)

***

<div id='lab1'>
    
# Laboratorio / Reto: Map/Reduce en Python con MRJOB
    
# 1. Creación ClusterEMR con CLI
    
## Descargar el CLI
    
- Primero se descarga el CLI desde la pagina de AWS 

![descarga](imagenes/descargando_CLI.png)

- Despues se configura el aws 

![config](imagenes/configurando_aws.png)

## Crear un S3
- Existen 2 formas de hacerlo la pagina de AWS o el CLI

### CLI
Para este lab se creó un s3 llamado `lab-reto-jjsanchezc`
```
aws s3 mb s3://lab-reto-jjsanchezc
```
    
si queremos ver que se creó correctamente podemos usar el comando 
```
aws s3 ls
```
o podemos verlo en aws como 

![s3existentes](imagenes/s3.png)

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
    --log-uri s3://lab-reto-jjsanchezc/logs/ \
    --applications Name=Hue Name=Spark Name=Hadoop Name=Sqoop Name=Hive \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large InstanceGroupType=TASK,InstanceCount=1,InstanceType=m4.large \
    --no-termination-protected
```
`--release-label` Especifica la versión de lanzamiento de Amazon EMR <br>
`--service-role` Especifica el rol de servicio de IAM <br>
`--ec2-attributes`Configuraciones de instancias de clúster y Amazon EC2.<br>
`--name` Nombre del cluster <br>
`--log-uri` <br>
`--applications` Aplicaciónes que se van a instalar en el cluster\<br>
`--instance-group` Especifica el numero y el tipo de instancias EC2 que se van a crear, aparte del rol que estas van a tomar, sea "MASTER", "CORE" ó "TASK" <br>
`--no-termination-protected` <br>

### Resultados 
- ### EC2

![cluster_ec2_res](imagenes/resultados_cluster_ec2.png)

- ### EMR

![cluster_emr_res](imagenes/resultados_cluster_emr.png)

![cluster_emr2_res](imagenes/resultados_cluster_emr2.png)

***
    
<div id='lab2'>

# 2.Conexión Main node del cluster

## conexión

para la conexion por SSH debemos usar la `"emr-key.pem"`:

cuando estemos dentro actualizaremos yum, instalamos pip, mrjob y luego git:

```
sudo yum update -y
sudo yum install git -y
sudo yum install python-pip -y
sudo pip3 install mrjob
```

se hace la copia del repo:

```
git clone https://github.com/ST0263/st0263-2023-1.git
```

Luego de haber clonado el repo se entra en el y se realizan los siguientes comandos: 

```
cd st0263-2023-1/"Laboratorio N6-MapReduce"/wordcount
python wordcount-local.py ../../datasets/gutenberg-small/*.txt > salida-serial.txt
```
si se hace el `sudo nano salida-serial.txt` veremos como se creó el archivo "salida-serial.txt" 
este es el resultado:

![wordcount-local](imagenes/resultado_worcount-local.png)

<br>

Ahora se quiere probar el mrjob local y se hace con el siguiente comando

```
python wordcount-mr.py ../../datasets/gutenberg-small/*.txt
```

Y sus resultados deberian ser:

![wordcount-mr](imagenes/resultado_wordcount-mr.png)

![wordcount-mr](imagenes/resultado_wordcount-mr2.png)


crear carpeta en hdfs 

```
hdfs dfs -mkdir /user/admin/
```

copiamos el dataset en el hdfs y ejecutamos

```
hdfs dfs -copyFromLocal /home/hadoop/st0263-2023-1/datasets/ /user/admin/
python wordcount-mr.py hdfs:///user/admin/datasets/gutenberg-small/*.txt -r hadoop --output-dir hdfs:///user/admin/result3
```

para ver los resultados en el result 

```
hdfs dfs -cat /user/admin/result3/*
```
proceso de ejecución y respuesta: 

![inicio](imagenes/inicio.png)

![progreso1](imagenes/map-reduce0.png)

![progreso2](imagenes/map100-reduce-0.png)

![result](imagenes/respuestamap.png)

***

<div id='reto'>
    
# Reto de programación en Map/Reduce

## para poder organizar mejor el README.md se decidió partirlo, para ver esta parte click en [ver](RetoProgramacion/README.md)

***
    
<div id='ref'>
    
## Referencias 

https://docs.aws.amazon.com/cli/latest/reference/emr/create-cluster.html <br>
PDF-Laboratorio-N6-Crear Cluster EMR-Hadoop <br>
https://docs.aws.amazon.com/es_es/cli/latest/userguide/cli-services-s3-commands.html <br>
https://mrjob.readthedocs.io/en/stable/guides/writing-mrjobs.html#defining-steps <br>
