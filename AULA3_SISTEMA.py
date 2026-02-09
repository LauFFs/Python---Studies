"""
Desafio 02 — Simulador Financeiro Mensal

Objetivo:
- Consolidar uso de tipos numéricos
- Realizar cálculos encadeados
- Gerar indicadores financeiros
- Produzir um relatório claro e profissional
"""

print("\nInforme os dados para o seu relatório financeiro mensal.\n")

# Dados pessoais
print("DADOS PESSOAIS")
nome = input("Nome: ")

# Dados financeiros
print("\nDADOS FINANCEIROS")
salario_bruto = float(input("Salário bruto: R$"))
if salario_bruto < 0:
    print("Entrada inválida. Encerrando análise.")
    exit()

beneficios = float(input("Benefícios: R$"))
if beneficios < 0:
    print("Entrada inválida. Encerrando análise.")
    exit()

descontos_fixos = float(input("Descontos fixos: R$"))
if descontos_fixos < 0:
    print("Entrada inválida. Encerrando análise.")
    exit()

# Renda total
renda_total = salario_bruto + beneficios

# Renda líquida
renda_liquida = renda_total - descontos_fixos
if renda_liquida <= 0:
    print("Renda líquida inválida para análise.")
    exit()

# Possui dívidas?
possui_dividas = input("Possui dívidas? Digite 'sim' ou 'nao': ").lower()
if possui_dividas != "sim" and possui_dividas != "nao":
    print("Entrada inválida. Encerrando análise.")
    exit()

# Poupa mensalmente?
reserva = 0
poupa_mensalmente = input("Poupa mensalmente? Digite 'sim' ou 'nao': ").lower()
if poupa_mensalmente == "sim":
    reserva = float(input("Qual o valor da sua reserva? R$"))
    if reserva < 0:
        print("Entrada inválida. Encerrando análise.")
        exit()
elif poupa_mensalmente == "nao":
    reserva = 0
    status_reserva = "INSUFICIENTE"
else:
    print("Entrada inválida. Encerrando análise.")
    exit()

# Gastos mensais
print("\nGASTOS MENSAIS")
total_gastos = float(input("Qual é o seu total de gastos? R$"))
if total_gastos < 0 or total_gastos > renda_liquida:
    print("Entrada inválida. Encerrando análise.")
    exit()

# Saldo final do mês
saldo = renda_liquida - total_gastos
# INDICADORES FINANCEIROS
# 1. Percentual de gastos sobre a renda líquida
percentual_gastos = (total_gastos / renda_liquida) * 100

# 2. Percentual de saldo sobre a renda líquida
percentual_saldo = (saldo / renda_liquida ) * 100

# Classificação financeira:
if percentual_gastos >= 80:
    classificacao_financeira = "CRÍTICO"
elif 50 <= percentual_gastos < 80:
    classificacao_financeira = "ATENÇÃO"
else:
    classificacao_financeira = "SAUDÁVEL"

# Análise da Reserva Financeira
if reserva != 0:
    if reserva < (renda_liquida * 3):
        status_reserva = "INSUFICIENTE"
    elif (renda_liquida * 3) <= reserva < (renda_liquida * 6):
        status_reserva = "RAZOÁVEL"
    else:
        status_reserva = "IDEAL"

# Regras de alerta
alerta_financeiro = "Nenhum alerta crítico identificado."
if classificacao_financeira == "CRÍTICO" and possui_dividas == "sim":
    alerta_financeiro = "Seu nível de gastos aliado à existência de dívidas indica risco financeiro imediato."

elif classificacao_financeira == "ATENÇÃO" and poupa_mensalmente == "nao":
    alerta_financeiro = "Seus gastos exigem atenção e a ausência de poupança aumenta o risco financeiro."

elif classificacao_financeira == "SAUDÁVEL" and status_reserva == "IDEAL":
    alerta_financeiro = "Você apresenta um excelente equilíbrio financeiro."

# Saldo redondo
if (saldo % 100) == 0:
    saldo_redondo = "Seu saldo mensal é um valor redondo e ótimo para planejamento."
else:
    saldo_redondo = "Seu saldo mensal não é um valor redondo para planejamento."

# Apresentação do relatório para o usuário
print(f'''\n==================================================
RELATÓRIO FINANCEIRO MENSAL

Nome: {nome}

Renda total:            R$ {renda_total:.2f}
Descontos fixos:        R$ {descontos_fixos:.2f}
Renda líquida:          R$ {renda_liquida:.2f}

Total de gastos:        R$ {total_gastos:.2f}

Saldo final:            R$ {saldo:.2f}

Percentual de gastos:   {percentual_gastos:.2f}%
Classificação:          {classificacao_financeira}

Reserva financeira:     R$ {reserva:.2f}
Status da reserva:      {status_reserva}

Hábitos financeiros:
- Possui dívidas:       {possui_dividas.upper()}
- Poupa mensalmente:    {poupa_mensalmente.upper()}

Indicadores:
- Gastos comprometem:   {percentual_gastos:.2f}% da renda liquida
- Saldo representa:     {percentual_saldo:.2f}% da renda líquida

Destaques:
- {saldo_redondo}
- {alerta_financeiro}
==================================================''')