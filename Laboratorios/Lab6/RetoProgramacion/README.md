# Reto de programación en Map/Reduce

Debido a que en estos retos nos pedían que estos se resolvieran en el EMR, debemos clonar este repo

```
git clone https://github.com/jjsanchezc/TopicosEnTelematica.git
cd Laboratorios/Lab6/RetoProgramacion
```
Luego de entrar al `RetoProgramacion` podemos ver que está separado en cada punto que se pedia, y dentro de estos puntos se encuentran sus respectivas datasets.txt

## Punto1

Se tiene un conjunto de datos, que representan el salario anual de los empleados formales en Colombia por sector económico, según la DIAN. ver su [dataset.txt](RetoProgramacion/punto1/dataset.txt) <br>

### Punto1a
El salario promedio por Sector Económico (SE) <br>
si desea ver el [codigo](RetoProgramacion/punto1/punto1a.py) <br>
se ejecuta el comando:

```
python punto1/punto1a.py dataset.txt
```

y su resultado es:

![respuesta1](imagenes/respuesta1a.png)

***

### Punto1b
El salario promedio por Empleado <br>
si desea ver el [codigo](RetoProgramacion/punto1/punto1b.py) <br>
se ejecuta el comando:

```
python punto1/punto1b.py dataset.txt
```

y su resultado es:

![respuesta1](imagenes/respuesta1b.png)

***

### Punto1c
Número de SE por Empleado que ha tenido a lo largo de la estadística <br>
si desea ver el [codigo](RetoProgramacion/punto1/punto1c.py) <br>
se ejecuta el comando:

```
python punto1/punto1c.py dataset.txt
```

y su resultado es:

![respuesta1](imagenes/respuesta1c.png)

***

# Punto2

Se tiene un conjunto de acciones de la bolsa, en la cual se reporta a diario el valor promedio por acción, la estructura de los datos es [dataset.txt](RetoProgramacion/punto2/dataset.txt) <br>

### Punto2a
Por acción, dia-menor-valor, día-mayor-valor <br>
si desea ver el [codigo](RetoProgramacion/punto2/punto2a.py) <br>
se ejecuta el comando:

```
python punto2/punto2a.py dataset.txt
```

y su resultado es:

![respuesta2a](imagenes/respuesta2a.png)

***

### Punto2b
Listado de acciones que siempre han subido o se mantienen estables <br>
si desea ver el [codigo](RetoProgramacion/punto2/punto2b.py) <br>
se ejecuta el comando:

```
python punto2/punto2b.py dataset.txt
```

y su resultado es:

![respuesta2b](imagenes/respuesta2b.png)

***

### Punto2c
DIA NEGRO: Saque el día en el que la mayor cantidad de acciones tienen el menor valor de acción (DESPLOME), suponga una inflación independiente del tiempo. <br>
si desea ver el [codigo](RetoProgramacion/punto2/punto2c.py) <br>
se ejecuta el comando:

```
python punto2/punto2c.py dataset.txt
```

y su resultado es:

![respuesta2c](imagenes/respuesta2c.png)

***

# Punto3
Sistema de evaluación de películas: Se tiene un conjunto de datos en el cual se evalúan las películas con un rating. Ver su [dataset.txt](RetoProgramacion/punto3/dataset.txt) <br>

### Punto3a
Número de películas vista por un usuario, valor promedio de calificación (SE) <br>
si desea ver el [codigo](RetoProgramacion/punto3/punto3a.py) <br>
se ejecuta el comando:

```
python punto3/punto3a.py dataset.txt
```

y su resultado es:

![respuesta3a](imagenes/respuesta3a.png)

***

### Punto3b
Día en que más películas se han visto <br>
si desea ver el [codigo](RetoProgramacion/punto3/punto3b.py) <br>
se ejecuta el comando:

```
python punto3/punto3b.py dataset.txt
```

y su resultado es:

![respuesta3b](imagenes/respuesta3b.png)

***

### Punto3c
Día en que menos películas se han visto <br>
si desea ver el [codigo](RetoProgramacion/punto3/punto3c.py) <br>
se ejecuta el comando:

```
python punto3/punto3c.py dataset.txt
```

y su resultado es:

![respuesta3c](imagenes/respuesta3c.png)

***

### Punto3d
Número de usuarios que ven una misma película y el rating promedio <br>
si desea ver el [codigo](RetoProgramacion/punto3/punto3d.py) <br>
se ejecuta el comando:

```
python punto3/punto3d.py dataset.txt
```

y su resultado es:

![respuesta3d](imagenes/respuesta3d.png)

***

### Punto3e
Día en que peor evaluación en promedio han dado los usuarios <br>
si desea ver el [codigo](RetoProgramacion/punto3/punto3e.py) <br>
se ejecuta el comando:

```
python punto3/punto3e.py dataset.txt
```

y su resultado es:

![respuesta3e](imagenes/respuesta3e.png)

***

### Punto3f
Día en que mejor evaluación han dado los usuarios <br>
si desea ver el [codigo](RetoProgramacion/punto3/punto3f.py) <br>
se ejecuta el comando:

```
python punto3/punto3f.py dataset.txt
```

y su resultado es:

![respuesta3f](imagenes/respuesta3f.png)

***

### Punto3g
La mejor y peor película evaluada por genero <br>
si desea ver el [codigo](RetoProgramacion/punto3/punto3g.py) <br>
se ejecuta el comando:

```
python punto3/punto3g.py dataset.txt
```

y su resultado es:

![respuesta3g](imagenes/respuesta3g.png)

***

[Volver](../README.md)