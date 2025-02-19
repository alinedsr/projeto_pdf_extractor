import os
import pandas as pd
from extract import extract_text_from_pdf, extract_data
from transform import transform_data
from load import save_to_csv, load_csv



if __name__ == "__main__":
    pdf_path = 'input/NATURA10.pdf'  # Caminho para o arquivo PDF de entrada
    csv_path = 'output/NATURA10.csv'  # Caminho para o arquivo CSV de saída
    main(pdf_path, csv_path)