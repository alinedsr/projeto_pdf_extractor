import pandas as pd
from transform import transform_data
from extract import extract_text_from_pdf, extract_data

def save_to_csv(df, csv_path):
    df.to_csv(csv_path, index=False, encoding='utf-8')

def load_csv(csv_path):
    return pd.read_csv(csv_path)

def main(pdf_path, csv_path):
    # Extrair dados do PDF
    text_by_page = extract_text_from_pdf(pdf_path)
    data = extract_data(text_by_page)

    # Criar DataFrame pandas com os dados extraídos
    df = pd.DataFrame(data)

    # Salvar temporariamente em um arquivo CSV intermediário
    temp_csv_path = 'temp.csv'
    save_to_csv(df, temp_csv_path)

    # Carregar o CSV intermediário
    df_loaded = load_csv(temp_csv_path)

    # Transformar os dados
    df_transformed = transform_data(df_loaded)

    # Salvar em um novo arquivo CSV
    save_to_csv(df_transformed, csv_path)

    # Remover o arquivo CSV temporário
    os.remove(temp_csv_path)

    print(f"Novo arquivo CSV '{os.path.basename(csv_path)}' criado com sucesso.")

