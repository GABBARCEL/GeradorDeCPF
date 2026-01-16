# IMPORTANTE!!!
# Antes de tudo, quero dizer que esse projeto foi feito apenas para fins educacionais, sem pretenção de uso ilegal ou comercial. Fique a vontade para usar de FORMA LEGAL. Esse algoritimo não revela dados pessoais ou dá qualquer acesso a qualquer informação confidencial!

from secrets import choice

seed = []
for i in range(9):
    seed.append(choice(range(10)))

def GenCpf(randomCPF):
    def calculoProdutos(CPF):
        PreVereficador = []
        peso = len(CPF) + 1
        for i in range(len(CPF)): # Gerando os produtos para somar depois e calcular os  DVs
            preSoma = CPF[i] * peso
            peso -= 1
            PreVereficador.append(preSoma)
        return PreVereficador


    # Parte de criação e atribuição do Dv1
    produtosDv1 = calculoProdutos(randomCPF)
    dv1 = (sum(produtosDv1) * 10 % 11)
    if dv1 == 10:
        dv1 = 0
    CPFcomDv1 = randomCPF + [dv1]

    #Parte de criação e atribuição do Dv2
    produtosDv2 = calculoProdutos(CPFcomDv1)
    dv2 = (sum(produtosDv2) * 10 % 11)
    if dv2 == 10:
        dv2 = 0


    CPF = ''.join(str(digito) for digito in (CPFcomDv1 + [dv2]))
    return CPF