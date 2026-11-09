
import pandas as pd
from pathlib import Path

# ==========================================
# 1. CAMINHO DA PLANILHA DE VENDAS
# ==========================================

caminho = Path(
    r"C:\Users\Matheus\Desktop\Cafe_Tambau_Vendas_Setembro.xlsx"
)

# ==========================================
# 2. CADASTRO DOS PRODUTOS
# ==========================================

produtos = {
    "P01": {"nome": "Café expresso", "categoria": "Bebida quente", "custo": 1.20},
    "P02": {"nome": "Cappuccino", "categoria": "Bebida quente", "custo": 2.80},
    "P03": {"nome": "Café com leite", "categoria": "Bebida quente", "custo": 1.60},
    "P04": {"nome": "Latte", "categoria": "Bebida quente", "custo": 2.40},
    "P05": {"nome": "Chá de capim-santo", "categoria": "Bebida quente", "custo": 0.90},
    "P06": {"nome": "Café gelado", "categoria": "Bebida fria", "custo": 3.10},
    "P07": {"nome": "Suco de laranja", "categoria": "Bebida fria", "custo": 2.60},
    "P08": {"nome": "Tapioca de queijo coalho", "categoria": "Salgado", "custo": 3.50},
    "P09": {"nome": "Tapioca de carne de sol", "categoria": "Salgado", "custo": 5.80},
    "P10": {"nome": "Pão de queijo", "categoria": "Salgado", "custo": 1.40},
    "P11": {"nome": "Cuscuz com ovo", "categoria": "Salgado", "custo": 3.20},
    "P12": {"nome": "Misto quente", "categoria": "Salgado", "custo": 3.00},
    "P13": {"nome": "Sanduíche natural", "categoria": "Salgado", "custo": 4.60},
    "P14": {"nome": "Croissant", "categoria": "Doce", "custo": 3.30},
    "P15": {"nome": "Bolo de macaxeira", "categoria": "Doce", "custo": 2.10},
    "P16": {"nome": "Brigadeiro", "categoria": "Doce", "custo": 0.90}
}

# ==========================================
# 3. IMPORTAR A PLANILHA DE VENDAS
# ==========================================

df = pd.read_excel(caminho, skiprows=1)

df.columns = df.columns.str.strip()

# ==========================================
# 4. TRATAMENTO DOS DADOS
# ==========================================

def converter_moeda(valor):

    if pd.isna(valor):
        return 0

    if isinstance(valor, (int, float)):
        return float(valor)

    valor = str(valor).replace("R$", "").strip()
    valor = valor.replace(".", "").replace(",", ".")

    return float(valor)


df["Total (R$)"] = df["Total (R$)"].apply(converter_moeda)

df["Qtde."] = pd.to_numeric(
    df["Qtde."], errors="coerce"
).fillna(0)

df["Cód. Produto"] = (
    df["Cód. Produto"].astype(str).str.strip()
)

# ==========================================
# 5. ADICIONAR DADOS DO CADASTRO
# ==========================================

df["Nome Produto"] = df["Cód. Produto"].map(
    lambda codigo: produtos.get(codigo, {}).get("nome")
)

df["Categoria"] = df["Cód. Produto"].map(
    lambda codigo: produtos.get(codigo, {}).get("categoria")
)

df["Custo Unitário"] = df["Cód. Produto"].map(
    lambda codigo: produtos.get(codigo, {}).get("custo")
)

# Verificar produtos sem cadastro
sem_cadastro = df[df["Custo Unitário"].isna()]

if not sem_cadastro.empty:
    print("ATENÇÃO: Produtos sem cadastro:")
    print(sem_cadastro["Cód. Produto"].unique())

df = df.dropna(subset=["Custo Unitário"])

# ==========================================
# 6. CALCULAR CUSTO E LUCRO
# ==========================================

df["Custo Total"] = df["Custo Unitário"] * df["Qtde."]

df["Lucro"] = df["Total (R$)"] - df["Custo Total"]

# ==========================================
# 7. RANKING POR PRODUTO
# ==========================================

ranking_produtos = (
    df.groupby(["Cód. Produto", "Nome Produto", "Categoria"])
    .agg(
        Quantidade_Vendida=("Qtde.", "sum"),
        Faturamento=("Total (R$)", "sum"),
        Custo_Total=("Custo Total", "sum"),
        Lucro_Total=("Lucro", "sum")
    )
    .reset_index()
    .sort_values("Lucro_Total", ascending=False)
)

# ==========================================
# 8. RANKING POR CATEGORIA
# ==========================================

ranking_categorias = (
    df.groupby("Categoria")
    .agg(
        Quantidade_Vendida=("Qtde.", "sum"),
        Faturamento=("Total (R$)", "sum"),
        Custo_Total=("Custo Total", "sum"),
        Lucro_Total=("Lucro", "sum")
    )
    .reset_index()
    .sort_values("Lucro_Total", ascending=False)
)

# ==========================================
# 9. FORMATAÇÃO MONETÁRIA
# ==========================================

def moeda(valor):
    return (
        f"R$ {valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

# ==========================================
# 10. EXIBIR RANKING DE PRODUTOS
# ==========================================

print("\n========== RANKING POR PRODUTO ==========\n")

for posicao, (_, produto) in enumerate(
    ranking_produtos.iterrows(), start=1
):

    print(f"{posicao}º - {produto['Nome Produto']}")
    print(f"Categoria: {produto['Categoria']}")
    print(f"Quantidade vendida: {produto['Quantidade_Vendida']:.0f}")
    print(f"Faturamento: {moeda(produto['Faturamento'])}")
    print(f"Custo total: {moeda(produto['Custo_Total'])}")
    print(f"Lucro total: {moeda(produto['Lucro_Total'])}")
    print("-" * 45)

# ==========================================
# 11. EXIBIR RANKING DE CATEGORIAS
# ==========================================

print("\n========== RANKING POR CATEGORIA ==========\n")

for posicao, (_, categoria) in enumerate(
    ranking_categorias.iterrows(), start=1
):

    print(f"{posicao}º - {categoria['Categoria']}")
    print(f"Quantidade vendida: {categoria['Quantidade_Vendida']:.0f}")
    print(f"Faturamento: {moeda(categoria['Faturamento'])}")
    print(f"Custo total: {moeda(categoria['Custo_Total'])}")
    print(f"Lucro total: {moeda(categoria['Lucro_Total'])}")
    print("-" * 45)

# ==========================================
# 12. RESUMO GERAL
# ==========================================

print("\n========== RESUMO GERAL ==========\n")

print(f"Faturamento: {moeda(df['Total (R$)'].sum())}")
print(f"Custo total: {moeda(df['Custo Total'].sum())}")
print(f"Lucro bruto: {moeda(df['Lucro'].sum())}")

print("\n==========================================")

