# Empezando a correr

## Reedirecciones

Para guardar las respuestas de la terminal en archivos .txt por ejemplo utilizo el flecha <b>></b>:
>$ ls .png > fotos.txt

Para seguir agregando info a un archivos existente utilzo doble fecha <b>>></b>:
>$ ls .jpeg >> fotos.txt

Para redireccionar el error utilizo <b>2></b>:
>$ ls .photo >> error.txt

Para direccionar ya sea la salida o el error utilizo:
>$ ls .photo > output.txt 2>&1

Nota: 1 es el output correcto y 2 es un error como respuesta.

Para guardar el input utilizo <b><</b>

## Otros comandos

echo imprime en la consola lo que le digamos:
>$ echo "Hola mundo"

>Hola mundo

cat permite concatenar archivos
>cat file1.txt file2.txt

## Pipe operator
Es un operador que permite tomar la salida de un comando y pasarla como entrada de otro comando. 

>$ |


## Operadores de control
Permite correr comandos de forma sincrona; uno detras del otro.
>$ ls; mkdir micarpeta

Para correr comandos en paralelo:
>$ mkdir micarpeta1 & mkdir micarpeta2

Para correr un comando detras de otro:
>$ mkdir micarpeta && cd /micarpeta

Operador or:
>$ ||


## Tipos de archivos

| Atributo | Tipo de archivo |
|----------|-----------------|
|-         |Un archivo normal|
|d         |Un directorio    |
|l         |Un link simbólico|
|b         |Un archivo de bloque especial. Son archivos que maneja la informacipon de los bloques de datos como una USB|

## Tipos de modos

|Dueño  |Grupo  |World  |
|-------|-------|-------|
|rwx    |r-x    |r~x    |
|111    |101    |101    |

## Modo simbólico

|Símbolo    |Significado    |
|-----------|---------------|
|u          |Solo para el usuarios  |
|g          |Solo para el grupo     |
|o          |Solo para otros (es el world)|
|a          |Aplica para todos      |


## Modificar permisos a los usuarios



## Variables de entorno
Para agregar un link simbolico (accesso directo):
>$ ls -s Documents/dev desarrollo

Para consultar links simbolicos
>$ ls -l

Para ver las variables de entorno:
>$ printenv


>$ echo $HOME


## grep
Encuentra coincidencias dentro de archivos

>$ grep Palabra archivo.csv


Nota: para buscar la palabra "the"

Para que no importe mayusculas o minusculas
>$ grep -i the archivo.cvs

Para contar la ocurrencia
>$ grep -c the archivo.csv

Para contar la ocurrencia ignorando si es mayusculas o minusculas
>$ grep -ci the archivo.csv

Para buscar aquellas lineas que no tengan "the":
>$ grep -vi the archivo.csv

Para contar palabras hay en un archivo:
>$ wc archivo.txt
























