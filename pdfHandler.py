from PyPDF2 import PdfFileReader

class PdfHandler(object):

    def __init__(self, pdfFile):
        self.openFile(pdfFile)

    def openFile(self, pdfFile):
        self.pdfObj = open(pdfFile, 'rb')
        self.pdf = PdfFileReader(self.pdfObj)

        self.info = self.pdf.getDocumentInfo()
        self.number_of_pages = self.pdf.getNumPages()

    def closePdf(self):
        self.pdfObj.close()

    def getNumberOfPages(self):
        return self.pdf.getNumPages();

    def getPdfMetadata(self):
        metadata = {}

        metadata["number_of_pages"] = self.number_of_pages
        metadata["info"] = {}
        metadata["info"]["default"] = self.info
        metadata["info"]['producer'] = self.info.producer
        metadata["info"]['author'] = self.info.author
        metadata["info"]['creator'] = self.info.creator

        return metadata

    def getText(self):
        text = ""
        text = self.pdf.getPage(4).extractText()
        # for pageNumber in range(1, self.number_of_pages):
        #     text = text + " " + self.pdf.getPage(pageNumber).extractText()

        return text
