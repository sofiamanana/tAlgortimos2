'''
Nombre: func2
Input: el arreglo A, la posicion de un elemento izq y la posicion de otro elemento der.
Return: retorna el total de desequilibrios en el arreglo.
Descripcion: divide el arreglo A en dos partes y se va llamando a si misma hasta que llega a una hoja, 
en este caso seria cuando el arreglo A contenga solo un elemento, una vez que llega al borde, continua
en el codigo y recorre los arreglos que recibe la funcion, que serian los cortes a la mitad del arreglo original.
Calcula los desequilibrios recorriendo todos los tamaños posibles entre izq y der y los va sumando.
'''

def func2(A,izq,der):

    if (izq == der):
        #Desequilibrio entre dos numeros iguales.
        return 0

    med = (izq + der)//2
    desequilibrio = 0
    I = func2(A,izq,med)
    D = func2(A,med+1,der)

    M=0

    for d in range(izq,med+1):
        for c in range(med+1,der+1):
            M += max(A[d:c]) - min(A[d:c])

    desequilibrio += (I+D+M)
    
    return desequilibrio

n = int(input())
arreglo = input().split(" ")
arreglo = list(map(int, arreglo))
print(func2(arreglo,0,n))
