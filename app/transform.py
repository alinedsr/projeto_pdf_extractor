import pandas as pd

def transform_data(csv_path):
    # Carregar o arquivo CSV
    df = pd.read_csv(csv_path)

    # Filtrar para remover linhas onde o campo "Pontos" é nulo
    df = df[df['Pontos'] != 'null']

    # Converter pontos para inteiro
    df['Pontos'] = df['Pontos'].apply(lambda x: int(x.split()[0]))

    # Criar a coluna "Preço Vigente"
    df['Preco Vigente'] = df.apply(lambda row: row['Preco Promocional'] if pd.notna(row['Preco Promocional']) else row['Preco Normal'], axis=1)

    # Selecionar apenas as colunas necessárias para o novo CSV
    df_novo = df[['Pagina', 'Codigo', 'Pontos', 'Preco Vigente']]

    return df_novo