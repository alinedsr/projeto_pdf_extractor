import re
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        text_by_page = []
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            text_by_page.append((page_num + 1, text))  # include page number
        return text_by_page

def extract_data(text_by_page):
    data = []
    for page_num, text in text_by_page:
        if text:
            # Use regular expressions to find all occurrences
            codes = re.findall(r'\((\d{5,6})\)', text)
            points = re.findall(r'(\d+)\s*pt[s]?', text)
            prices = re.findall(r'R\$\s*([\d,.]+)', text)
            promo_prices = re.findall(r'Por\s*R\$\s*([\d,.]+)', text)
            discounts = re.findall(r'economize\s*R\$\s*([\d,.]+)', text)

            max_len = max(len(codes), len(points), len(prices))

            for i in range(max_len):
                code = codes[i] if i < len(codes) else 'null'
                points_value = points[i] + ' pt' if i < len(points) else 'null'
                normal_price = 'R$ ' + prices[i] if i < len(prices) else 'null'
                promo_price = 'R$ ' + promo_prices[i] if i < len(promo_prices) else 'null'
                discount = 'R$ ' + discounts[i] if i < len(discounts) else 'null'

                if code != 'null':
                    data.append({
                        'Pagina': page_num,
                        'Codigo': code,
                        'Pontos': points_value,
                        'Preco Normal': normal_price,
                        'Preco Promocional': promo_price,
                        'Desconto': discount
                    })
    return data