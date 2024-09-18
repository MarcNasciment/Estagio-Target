#Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
#  faça um programa, na linguagem que desejar, que calcule e retorne:
#O menor valor de faturamento ocorrido em um dia do mês;
#O maior valor de faturamento ocorrido em um dia do mês;
#Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json

with open("dados.json") as faturamento_diario:
    dados = json.load(faturamento_diario)

def faturamento(dados):
    valores_faturados = [item["valor"] for item in dados if item["valor"] > 0]

    menor_faturamento = min(valores_faturados)
    maior_faturamento = max(valores_faturados)

    media_mensal = sum(valores_faturados) / len(valores_faturados)

    dias_acima_media = sum(1 for item in dados if item["valor"] > media_mensal)

    print(f"Menor valor de faturamento: R${menor_faturamento:,.2f}\n"
          f"Maior valor de faturamento: R${maior_faturamento:,.2f}\n"
          f"Número de dias com faturamento acima da média mensal: {dias_acima_media}\n")

faturamento(dados)
