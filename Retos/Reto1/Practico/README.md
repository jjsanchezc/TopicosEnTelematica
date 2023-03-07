# **RetoProgramación N1**
**Curso:** Tópicos Especiales en Telemática <br>
**Título:** Comunicación entre Procesos Remotos: gRPC.<br>
**Objetivo:** Desarrollar habilidades en la comunicación entre procesos distribuidos utilizando llamadas a procedimientos remotos (RPCs), especificamente gRPC.<br>
**Duración:** 35 mins.<br>
**Autores:** Juan José Sánchez Cortés - Estudiante de la Universidad EAFIT - [jjsanchezc](https://gist.github.com/jjsanchezc) <br>

***

**Tabla de Contenido**

1. [Introducción](#Introduccion)
2. [Estrucutra](#Estructura)
3. [Resultados](#Resultados)
4. [Desarrollo](#Desarrollo) 
5. [Despliegue](#Despliegue) <br>

***

<div id='Introduccion'/>

## **1. Descripción y alcance del proyecto.**
 Este reto tiene como fin, poder aplicar gRPC mediante el uso de una API Gateway y dos microservicios. Esta API debe recibir request desde postman, y poder procesar el pedido para poderle dar una respuesta al cliente <br>

***

 <div id='Estructura'/>

## **2. Estructura del Proyecto.**
Este proyecto está dividido en 3 partes:
- APIs (Python)
- Inventory (Go)
- ShoppingCart (Python)
### **APIs**
Dentro de esta carpeta hay un entorno virtual de python, nosotros solo nos enfocaremos en las carpetas llamadas "protobufs" y "src".
- protobufs:
   - Son los archivos .proto que usamos para conectar el API-Gateway con los microservicios
- src:
   - Se encuentra principalmente el servidor donde corre el API y todo el codigo gRPC que se generan de los .proto

### **Inventory**
En la carpeta de Inventory podemos encontrar un cambio de lenguaje (pasamos de Python a GoLang), por lo tanto tendremos carpetas nuevas, como lo son "go.mod" (tiene todas las librerias que se usan) y "go.sum" (describe la versión exacta que el compilador usará, haciendo que dicha compilación, sea fácil de reproducir).
Pero las carpetas principales son "ProductAvailability" y "src"
- ProductAvailability:
   - Se encuentra el archivo .proto y el codigo gRPC (en Go) que se generan de los .proto

- src:
   - Servidor del inventario y todos los procesos lógicos del inventario

### **ShoppingCart**
Hay un entorno virtual donde dentro de este se encuentran las respectivas carpetas. Pero al igual que en la carpeta de la API,solo nos enfocaremos en las carpetas "protobufs" y "src".
- protobufs:
   - Son los archivos .proto que usamos para conectar el API-Gateway con los microservicios
- src:
   - Se encuentra principalmente el servidor donde corre el API y todo el codigo gRPC (en Python) que se generan de los .proto
***

<div id='Resultados'/>

## En este punto por favor describa de igual forma, que patrones logró implementar.

## Resultados logrados
 Por favor describa claramente en puntos de lo solicitado logró alcanzar los objetivos propuestos. De igual forma, indique cuales objetivos no alcanzo a desarrollar. 

***

<div id='Desarrollo'/>

## Descripción técnica de la solución implementada: 
Por favor indique todos
los aspectos técnicos de la solución (librerías, como se debe compilar, etc,
con las versiones de cada elemento que utilice). Igualmente, todos los
aspectos de parametrización que se requiere, direcciones IPs, puertos,
conexión a bases de datos, etc.

***

<div id='Despliegue'/>

## Guía de uso
Por favor ilustre de manera clara, precisa y breve como se
utiliza su solución.
## Referencias
