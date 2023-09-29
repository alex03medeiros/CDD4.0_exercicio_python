brancos = int(input("Digite quantos votos brancos teve: "))
nulos = int(input("Digite quantos votos nulos teve: "))
validos = int(input("Digite quantos votos validos teve: "))

eleitores = brancos+nulos+validos

perB = (brancos/eleitores) * 100
perN = (nulos/eleitores) * 100
perV = (validos/eleitores) * 100

print("O numero de eleitores foi {}.".format(eleitores))
print("Sendo brancos {}%, nulos {}%, validos {}% ".format(perB,perN,perV))