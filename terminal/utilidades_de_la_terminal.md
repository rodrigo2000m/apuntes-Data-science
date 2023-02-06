# Utilidades de la terminal

## Utilidades de red
Información de la red:
>$ ifconfig

Para revisar si estamos conectados a una pagina:
>$ ping www.google.com

Trae archivos desde una url:
>$ curl www.google.com   #devuelve el html en este caso

Para traer cosas desde la red (descarga el archivo directamente):
>$ wget www.google.com

Cuando nos conectamos a un sitio nos dice a que computadoras nos estamos conectando:
>$ traceroute www.google.com

Para mostrarnos nuestros dispositivos de red:
>$ netstat -i


## Comprimir archivos .tar y .zip
>$ tar -cvf carpeta.tar carpetaName

>$ tar -cvzf carpeta.tar.gz carpetaName

Para descomprimir:
>$ tar -xvf carpeta.tar

>$ tar -xzvf carpeta.tar.gz

Para comprimir en .zip:
>$ zip -r comprimiZip.zip carpetaName

>$ unzip -r comprimiZip.zip


## Manejo de procesos
Para ver procesos que estan corriendo:
>$ ps

Para matar un proceso:
>$ kill 12345 #no. de id

Para ver procesos que en funcion de los recusos que consument:
>$ top
>$ htop

## Editores de texto dentro de la  terminal
>$ vim



