#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: luozaibo
# date : 2019-10-09 13:01:36

import os
from PyPDF2 import PdfFileReader, PdfFileWriter
 
def pdf_split(pdf):
    pdf_reader = PdfFileReader(pdf)
    pdf_writer = PdfFileWriter()
    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page)) 
    output_filename = f'info_{page}.pdf'
    with open(output_filename, 'wb') as f:
        pdf_writer.write(f)       

def get_info(pdf):
    pdf_reader = PdfFileReader(f)
    with open(pdf, 'rb') as f:
        info = pdf_reader.getDocumentInfo()
        pages = pdf_reader.getNumPages()
    print(info)
    print(pages)

def merge_pdf(pdfs):
    pdf_writer = PdfFileWriter()
    for pdf in pdfs:
        pdf_reader = PdfFileReader(pdf)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open('merge.pdf', 'wb') as f:
        pdf_writer.write(f)

def custom_split(pdf):
    pdf_reader = PdfFileReader(pdf)
    pdf_writer = PdfFileWriter()
    page_count = pdf_reader.getNumPages()
    print(page_count)
    for page in range(3):
        pdf_writer.addPage(pdf_reader.getPage(page))
    with open('custom.pdf', 'wb') as f:
        pdf_writer.write(f)

    i = PdfFileReader('custom.pdf').getNumPages()
    print(i)


if __name__ == '__main__':
    # path = 'info.pdf'
    # pdfs = ['info_3.pdf', 'info_4.pdf']
    # pdf_split(path)
    # get_info(path)
    # merge_pdf(pdfs)
    custom_split('info.pdf')

