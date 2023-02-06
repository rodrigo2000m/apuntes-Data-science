# Paquetes en py
Un paquete es una carpeta con diferentes modulos.

<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">


<i class="material-icons" style="font-size:20px;">folder</i> pkg
- mod_1.py
- mod_2.py


Al momento de importar las funciones desde un paquete:
```py
from pkg.mod_1 import func_1, func_2
from pkg.mod_2 import func_3, func_4

# utilizó las funciones como si las hubiese definido en el propio archivo
# los nombres de las funciones no deben chocar
```
