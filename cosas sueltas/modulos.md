# Modulos de py

## Qué son?
Nos permite establecer bloques de código o lógica en diferentes archivos.

## Importación de modulos
```py
import modul_name # importo todo el modulo

from modul_name import func_name, func_name # importo las funciones que quiero utilizar
```

## Módulos comunes
```py
#para trabajar con el sistema operativo
import sys 

#para expresiones regulares
import re
text = "lorem 3 ipsum 34"
result =re.findall("[0-9]+", test) # result=[3, 34]

#para trabajar con tiempo
import time
time.time() #formato de compu
local =time.localtime() #hora local
time.asctime(local) #hora local en formato entendible ASC: Mon Oct 3 23;56;24 2022

#para manejar listas
import collections
num=[1,1,3,4,5,5,2,3]
counter = collections.Counter(num) #devuelve la frecuencia{1:2, 2:1, 3:2, 4:1, 5:2}
```

## ¿Cómo crear módulos propios?
Son solo archivos <b>.py<b>:
>mod.py
```py
def get_population():
    key = ["col", "bol"]
    values = [300, 400]
    return keys, values
```
<br>

#### Desde otro archivo lo importo y utilizó las funciones de este:

>main.py
```py
import mod #no se coloca el .py
leys, values = mod.get_population()
print(keys, values)
```

## Otras formas de correr módulos
- importando el módulo
- ejecutando el archivo desde consola

#### Cuando se ejecuta el archivo main desde otro archivo, o sea se esta usando como un modulo es importante tener controlo de cuando se ejecutan las funciones de <b>main.py</b> y de <b>mod.py</b>

>main.py
```py
# lafuncion run() se ejecuta si y solo si main.py es corrido desde la terminal
if __name__ == "__main__": 
    run() #todo el codigo anterior se coloca dentro de una funcion run()
```

