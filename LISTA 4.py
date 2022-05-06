from re import X
lista=[]
valor=int(input("Digite la lista: "))
while valor in range(5):
    lista.append(valor)
    if lista < 0:
        b=int(input("Digite un numero positivo: "))
        print(b)
    

