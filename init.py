from pdfHandler import PdfHandler

pdf_bigger = 'pdftests/pdf_bigger.pdf'
pdf_smaller = 'pdftests/pdf_smaller.pdf'
pdf = PdfHandler(pdf_bigger)
# info = pdf.getPdfMetadata()
text = pdf.getText()
# numPages = pdf.getNumberOfPages()
pdf.closePdf()
# print info
print text
# print numPages
