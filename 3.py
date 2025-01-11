import json

# Carregar os dados
with open("dados.json") as file:
    dados = json.load(file)

# Filtrar dias com faturamento (excluir zeros)
faturamento = [dia["valor"] for dia in dados if dia["valor"] > 0]

# Calcular resultados
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)
dias_acima_media = sum(1 for valor in faturamento if valor > media_mensal)

# Exibir resultados
print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias acima da média mensal: {dias_acima_media}")
