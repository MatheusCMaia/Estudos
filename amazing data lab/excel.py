
import pandas as pd
from pathlib import Path

# Caminho da planilha
caminho = Path(
    r"C:\Users\Matheus\Desktop\Cafe_Tambau_Vendas_Setembro.xlsx"
)

# Ler a planilha, ignorando a primeira linha vazia
df = pd.read_excel(caminho, skiprows=1)

# Remover espaços extras dos nomes das colunas
df.columns = df.columns.str.strip()

# Função para converter valores monetários
def converter_moeda(valor):

    if pd.isna(valor):
        return 0

    # Se já for número, não precisa remover separadores
    if isinstance(valor, (int, float)):
        return float(valor)

    # Converter texto para número
    valor = str(valor).replace("R$", "").strip()

    # Formato brasileiro: 1.234,56
    valor = valor.replace(".", "").replace(",", ".")

    return float(valor)


# Converter coluna de faturamento
df["Total (R$)"] = df["Total (R$)"].apply(converter_moeda)

# Garantir que quantidade seja numérica
df["Qtde."] = pd.to_numeric(df["Qtde."], errors="coerce").fillna(0)

# Calcular faturamento total
faturamento_total = df["Total (R$)"].sum()

# Calcular quantidade total de produtos vendidos
quantidade_total = df["Qtde."].sum()

# Agrupar faturamento por canal
vendas_por_canal = (
    df.groupby("Canal")["Total (R$)"]
    .sum()
    .sort_values(ascending=False)
)

# Agrupar quantidade por canal
quantidade_por_canal = (
    df.groupby("Canal")["Qtde."]
    .sum()
    .sort_values(ascending=False)
)

# Calcular participação percentual
participacao = (vendas_por_canal / faturamento_total) * 100

# Exibir resultados
print("\n========== RESULTADO DAS VENDAS ==========")

print(f"\nFaturamento total: R$ {faturamento_total:,.2f}")
print(f"Quantidade total de produtos vendidos: {quantidade_total:.0f}")

print("\n========== FATURAMENTO POR CANAL ==========")

for canal, valor in vendas_por_canal.items():
    print(f"{canal}: R$ {valor:,.2f}")

print("\n========== QUANTIDADE POR CANAL ==========")

for canal, quantidade in quantidade_por_canal.items():
    print(f"{canal}: {quantidade:.0f} unidades")

print("\n========== PARTICIPAÇÃO POR CANAL ==========")

for canal, percentual in participacao.items():
    print(f"{canal}: {percentual:.2f}%")

print("\n===========================================")
