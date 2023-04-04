def calculaFatorial (horaAtual):
    cont = 1
    fatorial = 1

    while cont <= horaAtual:
        fatorial *= cont
        cont += 1

    print(f'A Senha é LIBERDADE{fatorial}')

horaAtual = int(input('Para desbloquear o sistema insira os minutos que estão na sua máquina: '))
calculaFatorial(horaAtual)