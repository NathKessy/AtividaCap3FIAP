def pulaLinha():
    print("")

def cabecalho():
    print ("----------------------------------")
    print ("Planos de assinatura do YouTube")
    print ("----------------------------------")

def exibePlanos():
    print ("Qual plano você deseja fazer ? ")
    print ("1 - Basic com 30% sobre o faturamento")
    print ("2 - Silver com 20% sobre o faturamento")
    print ("3 - Gold com 10% sobre o faturamento")
    print ("4 - Platinum 5% sobre o faturamento")
    pulaLinha()
    
def validaPlano(planoSelecionado, faturamentoAnual):
    calculaPlano = 0
    if (planoSelecionado == 1):
        calculaPlano = faturamentoAnual * 0.3
        print ("O plano selecionado foi Basic.")
    elif (planoSelecionado == 2):
        calculaPlano = faturamentoAnual * 0.2
        print ("O plano selecionado foi Silver.")
    elif (planoSelecionado == 3):
        calculaPlano = faturamentoAnual * 0.1
        print ("O plano selecionado foi Gold.")
    elif (planoSelecionado == 4):
        calculaPlano = faturamentoAnual * 0.05
        print ("O plano selecionado foi Platinum.")
    else:
        pulaLinha()
        print ("**** INSIRA UM PLANO VALIDO ****")
        pulaLinha()
    
    return calculaPlano;

def exec():
    isValido = True
    calculaPlano = 0.0

    cabecalho()
    print ("Bem vindo")
    faturamentoAnual = float(input("Digite seu faturamento anual: "))
    pulaLinha()

    while isValido:  
        exibePlanos()
        planoSelecionado = float(input("Digite o número do plano escolhido: "))
        pulaLinha()
        calculaPlano = validaPlano(planoSelecionado, faturamentoAnual)
        if (calculaPlano > 0):
            isValido = False
    print ("A porcetagem sobre o faturamento do seu plano é de R$ {}.".format(calculaPlano))


#Iniciando Programa
exec()
