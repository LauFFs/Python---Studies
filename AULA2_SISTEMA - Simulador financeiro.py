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
beneficios = float(input("Benefícios: R$"))
descontos_fixos = float(input("Descontos fixos: R$"))

# Gastos mensais
print("\nGASTOS MENSAIS")
moradia = float(input("Moradia: R$"))
alimentacao = float(input("Alimentação: R$"))
transporte = float(input("Transporte: R$"))
lazer = float(input("Lazer: R$"))
outros_gastos = float(input("Outros gastos: R$"))

# Renda total
renda_total = salario_bruto + beneficios

# Total de gastos
total_gastos = moradia + alimentacao + transporte + lazer + outros_gastos

# Renda líquida
renda_liquida = renda_total - descontos_fixos

# Saldo final do mês
saldo = renda_liquida - total_gastos

# INDICADORES FINANCEIROS
# 1. Percentual de gastos sobre a renda líquida
percentual_gastos = (total_gastos / renda_liquida) * 100

# 2. Percentual de saldo sobre a renda líquida
percentual_saldo = (saldo / renda_liquida ) * 100

# Apresnetação do relatório para o usuário
print(f'''\n==================================================
RELATÓRIO FINANCEIRO MENSAL

Nome: {nome}

Renda total:            R$ {renda_total:.2f}
Descontos fixos:        R$ {descontos_fixos:.2f}
Renda líquida:          R$ {renda_liquida:.2f}

Total de gastos:        R$ {total_gastos:.2f}
- Moradia:              R$ {moradia:.2f}
- Alimentação:          R$ {alimentacao:.2f}
- Transporte:           R$ {transporte:.2f}
- Lazer:                R$ {lazer:.2f}
- Outros:               R$ {outros_gastos:.2f}

Saldo final:            R$ {saldo:.2f}

Indicadores:
- Gastos compromentem:  {percentual_gastos:.2f}% da renda liquida
- Saldo representa:      {percentual_saldo:.2f}% da renda líquida
==================================================''')
