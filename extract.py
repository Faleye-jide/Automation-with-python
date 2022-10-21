import PyPDF2
from pathlib import Path
from datetime import datetime


def extract_info(pdf_path):
    # create a pdf file object
    with open(pdf_path, 'rb') as pdfFileObj:
        # create a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        info = pdfReader.getDocumentInfo()
        number_of_pages = pdfReader.getNumPages()
        
        
         # print(pdfReader)
        # printing number of pages in the pdf
        number_of_pages = pdfReader.numPages
            # print(number_of_pages)

        # create a page object to grab the pages
        pageObj = pdfReader.getPage(0)
        # print(pageObj)

        # extract text from the page 
        text = pageObj.extractText()
    
    return text

    txt = f'''
    Information about {pdf_path}:
    
    Author: {info.author}
    Creator: {info.creator}
    Number_of_pages: {number_of_pages}

    '''
    
    # return txt
    
    



if __name__ == '__main__':
    pdf_path = 'Jide_Faleye_CV.pdf'
    print(extract_info(pdf_path))