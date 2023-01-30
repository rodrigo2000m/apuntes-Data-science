# Comandos básicos de la terminal

## Variantes de ls
Devuelve los archivos visibles que se encuentran en el directorio actual:
>$ ls

Para visualizar los archivos visibles y los <b>archivos ocultos</b>:
>$ ls -la

Para obtener los archivos ordenados por tamaño:
>$ ls -lS

Me los ordena alfabeticamente al reves:
>$ ls -lr

Para desplegar todos los archivos como un árbol (funciona en WS):
>$ tree

>$ tree -L 2 #profundiza en 2 niveles


## Crear y modificar carpetas
Crear carpetas:
>$ mkdir mi_carpeta

Para colocar nombre de carpetas con espacios uso comillas:
>$ mkdir "mi carpeta"

Para crear archivos:
>$ touch filename

Copiar archivos:
>$ cp file_origin ../file_blank

Mover archivos:
>$ mv file_origin path

Renombrar archivos o carpeta:
>$ mv file_origin file_bk

Borrar archivos:
>$ rm file

>$ rm -i file #me pide confirmacion

Borrar carpetas:
>$ rm -r directorio

>$ rm -ri directorio

>$ rm -rf #borrar de forma forzada

## Exploración de archivos

Para visualizar las primeras 10 lineas de un archivo:

>$ head file.txt

Para cambiar la cantidad de lineas que visualizo (por ejemplo 15 lineas):
>$ head file.txt -n 15

Para leer las últimas 15 líneas de un archivo:
>$ tail file.txt -n 15 

Para abrir el archivo como con vim:
>$ less file.txt

Para salir solo esq y q

Para abrir un archivo desde un programa predeterminado:
>$ xdg-open file.txt

Se abre un proceso en la términal que nos muestra información.

Para abrir la carpeta de archivos desde la terminal (en linux):
>$ nautilus Documents/


## Comandos
>$ type comando

Me devuelve a que tipo de comando pertenece

## Alias
Los alias son temporales
>$ alias  l="ls -lh"

Manual y ayuda:
>$ help cd

>$ man man 

>$ info cd

>$ what is cd

## Wildcards
Caracteres especiales para busquedas optimizadas.
>$ ls *.txt

Archivos que tengan "datos" en su nombre:
>$ ls datos*

Archivos que tengan "datos" en su nombre y dos caracteres más:
>$ ls datos??

Archivos (incluso que esten dentro de las carpetas de niveles menores) que comiencen con mayúscula:
>$ ls [[:upper:]]*

Para no buscar en los archivos que esten dentro de las carpetas:
>$ ls -d [[:upper:]]*




















