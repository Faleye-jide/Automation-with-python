from PyPDF2 import PdfFileReader, PdfFileWriter
import time


def rotate_pages(pdf_path, output):
    pdf_writer = PdfFileWriter()
    pdfReader = PdfFileReader(pdf_path)

    # rotate the first page 
    page_1 = pdfReader.getPage(0).rotate_clockwise(90)
    # write the page to a new pdf
    pdf_writer.addPage(page_1)

    print('Getting started with the operation')
    with open(output, 'wb') as output:
        pdf_writer.write(output)
        
    time.sleep(4)
    print('Executed successfully')
        

if __name__ == '__main__':
    pdf_path = 'Jide_Faleye_CV.pdf'
    output = 'result.pdf'
    rotate_pages(pdf_path, output)
