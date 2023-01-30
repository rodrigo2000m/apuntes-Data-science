# Manipulación de archivos y errores

## Iterables
```py
my_iter = iter(range(1,11))
print(next(my_iter)) #itero de a uno, cuando ejecuto me a 1, luego 2, 3, 4, etc. Cuando se termina me devuelve StopIter
```

## Errores en Python

Cuando hay un error el programa se para
```py
suma = lambda x,y = x+y
assert suma(2,2)==4 #testeo que me de un error
```

Para producir un excepción propio:

```py
age = 10
if age < 18:
    raise Exception("No se permiten menores") # devuelve este mensaje y se detiene el programa
```

## Manejo de excepciones
```py
try:
    print(0/0)
except ZeroDivisionError as error
    print(error) # no se detiene el programa, selo devuelve el error

#en el lugar de ZeroDivisionError debo colocar el tipo de error que me esta devolviendo la consola

```


## Leer archivos de texto

```py
file = open("./text.txt")
file.read() #lee todo el archivo de una

file.readline() #lee linea a linea, se suele incluir en un for:
for line in file:
    return line

file.close()

#abrir el archivo y cerrarlo cuando se termine de leer:
with open("./text.txt") as file:
    for line in file:
        return line
```

## Escribir en un archivo

```py
#r, w, r+ (escritura y lectura), w+(escritura y lectura pero reescribiendo el archivo) 
with open("./text.txt", "r+") as file:
    for line in file:
        return line
    file.write("nuevas cosas en este archivo")
```

## Leer un csv
>read_csv.py
```py
import csv

def read_csv(path):
    with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter =",")
    for row in reader:
        print("***"*5)
        print(row)

#para ejecutar desde el archivo y desde consola
if __name__ == "__main__":
    read_csv("./app/data.csv")
```

Si quisiera convertir los datos en una lista de diccionarios:

>read_csv.py
```py
import csv

def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter =",")
        header = next(reader) #me guardar los nombres de las columnas

    data = []
    for row in reader:
        iterable =zip(header, row)
        print(list(iterable)) # hasta este punto me lo guarda como una lista de tuplas

        country_dict = {key: vaule for key, value in iterable}
        data.append(country_dict)
#para ejecutar desde el archivo y desde consola
if __name__ == "__main__":
    read_csv("./app/data.csv")
```













