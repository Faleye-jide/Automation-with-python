from PyPDF2 import PdfFileReader, PdfFileWriter
import time


def merge_pdfs(pdf_paths, output):
    
    # create a pdf writer object to
    pdf_writer = PdfFileWriter()
    
    # iterate through the pdf_paths
    
    for pdf in pdf_paths:
        # create a pdf reader object for each pdf
        pdf_reader = PdfFileReader(pdf)
        # get the pages in each pdf and add to the writer object
        for page in range(pdf_reader.getNumPages()):
            print(page)
            pdf_writer.addPage(pdf_reader.getPage(page))
            
    # write the merged pdf to a file
    
    with open(output, 'wb') as outfile:
        pdf_writer.write(outfile)
        


if __name__ == "__main__":
    pdf_paths = ['Jide_Faleye_CV.pdf','result.pdf']
    output = 'merged.pdf'
    merge_pdfs(pdf_paths, output)
        
       