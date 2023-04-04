def pulaLinha():
    print("")

def cabecalho(nomeEscola):
    print (f'Escola de inglês {nomeEscola}')
    print ("--------------------------------")
    pulaLinha()
    print (f'Bem vindo ao sistema de notas da escola de inglês {nomeEscola}')
    pulaLinha()

def calculaMediaPares():
    pulaLinha()
    somaNotasPares = 0

    print("Você está digitando a notas dos alunos com números pares da chamada")
    for cont in range (2,51,2):
        notaAlunosPares = float(input(f'Por favor, insira a nota do aluno de numero {cont}: '))
        somaNotasPares += notaAlunosPares
    return somaNotasPares / 25

def calculaMediaImpar():
    somaNotasImapares = 0

    pulaLinha()
    print("Você está digitando a notas dos alunos com números impares da chamada")
    for cont in range (1,50,2):
        notaAlunosImapres = float(input(f'Por favor, insira a nota do aluno com o numero {cont}: '))
        somaNotasImapares += notaAlunosImapres
    return somaNotasImapares / 25

def validaMedia():
    mediaimpar = calculaMediaImpar()
    mediaPar = calculaMediaPares()
    if (mediaPar > mediaimpar):
        pulaLinha()
        print (f'A turma com a maior media foi a par com {mediaPar}.')
        print(f'E a media da turma impar foi de {mediaimpar}.')
    else:
        pulaLinha()
        print (f'A turma com a maior media foi a impar com {mediaimpar}.')
        print(f'E a media da turma par foi de {mediaPar}.')   

def exec():
    cabecalho("JoWell Sant’ana")
    validaMedia()

#Iniciando Programa
exec()

