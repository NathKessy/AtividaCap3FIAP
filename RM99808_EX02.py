def pulaLinha():
    print("")

print ("    VOTAÇÃO DAS AULAS   ")
print ("------------------------")
pulaLinha()

validador = 0
resultado = ""

print ("Informe a quantidade de votos")
segunda = int(input("Informe a quantidade de votos para ter aulas na segunda-feira ? "))
terca = int(input("Informe a quantidade de votos para ter aulas na terça-feira ? "))
quarta = int(input("Informe a quantidade de votos para ter aulas na quarta-feira ? "))
quinta = int(input("Informe a quantidade de votos para ter aulas na quinta-feira ? "))
sexta = int(input("Informe a quantidade de votos para ter aulas na sexta-feira ? "))

if validador < segunda:
    validador = segunda
if validador < terca:
    validador = terca
if validador < quarta:
    validador = quarta
if validador < quinta:
    validador = quinta
if validador < sexta:
    validador = sexta

if (validador == segunda):
    resultado = "Segunda "
if (validador == terca):
    resultado = resultado + "Terça "
if (validador == quarta):
    resultado = resultado + "Quarta "
if (validador == quinta):
    resultado = resultado + "Quinta "
if (validador == sexta):
    resultado = resultado + "Sexta"

if (len(resultado) <= 8 ):
    print ("O resultado da votação foi um total de {} votos e o dia que foi escolhido foi {}.".format(validador, resultado))
else:
    print("O resultato empatou entre os dias {} e a quantidade de votos foi de {} para cada dia.".format(resultado.split(), validador))