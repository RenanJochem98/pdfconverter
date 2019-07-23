from pdfHandler import PdfHandler

pdf_bigger = 'pdftests/pdf_bigger.pdf'
pdf_smaller = 'pdftests/pdf_smaller.pdf'
pdf = PdfHandler(pdf_smaller)
# info = pdf.getPdfMetadata()
text = pdf.getText()
pdf.closePdf()
print text
