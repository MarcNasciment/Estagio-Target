#Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#Escreva um programa na linguagem que desejar onde calcule o percentual de representação
# que cada estado teve dentro do valor total mensal da distribuidora.  

faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "OUTROS": 19849.53
}

faturamento_total = sum(faturamento_estados.values())

percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estados.items()}

for estado, percentual in percentuais.items():
    print(f"Percentual {estado}: {percentual:.2f}%")