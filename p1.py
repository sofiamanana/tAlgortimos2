'''
Nombre: func.
Input: un array, un entero n que es el tamaño del arreglo y un entero s que es el tamaño de los grupos a formar.
Return: el maximo de las minimas distancias.
Descripcion: en el codigo vamos probando consecutivamente si podemos descubrir una minima diferencia con el 
promedio de derecha a izquierda. Si logramos encontrar s diferentes puntos del array con la minima diferencia, se guarda y 
se analiza el lado derecho del array (desde el medio), si no, se analiza el lado izquierdo.
'''

def func(array,n,s):

    minimo=0
    der=array[n-1]-array[0]
    izq=0

    while(der>=izq):
        med =(der+izq)//2
        flag=False
        cant=1
        lugar=0

        for d in range(1, n):
            if(array[d]-array[lugar]>=med ):
                lugar=d
                cant+=1
                if(cant==s):
                    flag=True

        if(flag):
            minimo=med
            izq=med+1

        else:
            der=med-1

    return minimo

inputList = input().strip().split(" ")
arreglo = input().strip().split(" ")
arreglo = list(map(int, arreglo))
print("s = ",func(arreglo, int(inputList[0]),int(inputList[1])))




