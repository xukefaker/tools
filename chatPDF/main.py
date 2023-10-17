import pdfplumber

with pdfplumber.open('test.pdf') as pdf:
    first_page = pdf.pages[1]
    for line in first_page.extract_text_lines(layout=True):
        print(line['text'] + ' ')