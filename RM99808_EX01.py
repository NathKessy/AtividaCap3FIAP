def cabecalho():
    print ("----------------------------------")
    print ("Planos de assinatura do YouTube")
    print ("----------------------------------")

def exibePlanos():
    print ("Qual plano você deseja fazer ? ")
    print ("1 - Basic")
    print ("2 - Silver")
    print ("3 - Gold")
    print ("4 - Platinum")
    
def validaPlano(planoSelecionado, faturamentoAnual):
    calculaPlano = 0
    if (planoSelecionado == 1):
        calculaPlano = faturamentoAnual * 0.3
    elif (planoSelecionado == 2):
        calculaPlano = faturamentoAnual * 0.2
    elif (planoSelecionado == 3):
        calculaPlano = faturamentoAnual * 0.1
    elif (planoSelecionado == 4):
        calculaPlano = faturamentoAnual * 0.05
    else:
        print("")
        print ("**** INSIRA UM PLANO VALIDO ****")
        print("")
    
    return calculaPlano;

def exec():
    isValido = True
    calculaPlano = 0.0

    cabecalho()
    print ("Bem vindo")
    faturamentoAnual = float(input("Digite seu faturamento anual: "))

    while isValido:  
        exibePlanos()
        planoSelecionado = float(input("Digite o número do plano escolhido: "))
        calculaPlano = validaPlano(planoSelecionado, faturamentoAnual)
        if (calculaPlano > 0):
            isValido = False
    print ("O faturamento do seu plano é de R$ {}".format(calculaPlano))


#Iniciando Programa
exec()
