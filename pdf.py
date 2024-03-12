import PyPDF2
import os

def birlestir_pdf(pdf_dizin, cikti_pdf):
    pdf_merger = PyPDF2.PdfFileMerger()

    # PDF dosyalarını birleştir
    for dosya_adi in os.listdir(pdf_dizin):
        if dosya_adi.endswith('.pdf'):
            pdf_merger.append(os.path.join(pdf_dizin, dosya_adi))

    # Birleştirilmiş PDF'yi kaydet
    with open(cikti_pdf, 'wb') as cikti:
        pdf_merger.write(cikti)

    print("PDF'ler başarıyla birleştirildi.")

# PDF dosyalarının bulunduğu dizin ve birleştirilmiş PDF'nin adı
pdf_dizin = '/path/to/pdf/dizin/'
cikti_pdf = '/path/to/birlestirilmis.pdf'

birlestir_pdf(pdf_dizin, cikti_pdf)