idade = int(input("Digite a sua idade: "))
mes = int(input("Digite o mes que voce nasceu: "))
dia = int(input("Digite o dia: "))

somaI = idade * 365
somaM = mes * 30
somaD = 30 - dia
total = somaI + somaD + somaM

print("Voce ja viveu {} dias.".format(total))