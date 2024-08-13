import os
from pypdf import PdfWriter

# Cria uma instância do PdfWriter
writer = PdfWriter()

# Lista os arquivos da pasta "arquivos" e ordena
lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()

# Valida se os arquivos são da extensão PDF e faz o merge
for arquivo in lista_arquivos:
    if arquivo.endswith(".pdf"):
        # Abre o arquivo PDF e adiciona ao writer
        with open(f"arquivos/{arquivo}", "rb") as pdf_file:
            writer.add_page_from_reader(pdf_file)

# Salva o arquivo final
with open("PDF_final.pdf", "wb") as output_pdf:
    writer.write(output_pdf)
