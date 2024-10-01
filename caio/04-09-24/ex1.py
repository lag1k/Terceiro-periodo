valor = int(input("Digite seu valor: \n -> "))
list = []

def ex(valor) :
    for i in range (valor + 1) :
        list.append(i)
    r1 = sum(list)
    print(f"Seu numero foi {valor} \n a soma de todos os numeros é {r1}")

ex(valor)

