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

def merge_pdf(pdfs):
    pdf_writer = PdfFileWriter()
    print(pdfs)
    for pdf in pdfs:
        pdf_reader = PdfFileReader(pdf)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open('merge.pdf', 'wb') as f:
        pdf_writer.write(f)

    print(f'合并成功 merge.pdf')

def custom_split(pdf):
    pdf_reader = PdfFileReader(pdf)
    pdf_writer = PdfFileWriter()
    page_count = pdf_reader.getNumPages()
    print(f'一共{page_count} 页')
    try:
        section = input('输入分割起始页数(以空格分开):')
        start = int(section.split()[0])
        end = int(section.split()[1])
        for page in range(start, end+1):
            pdf_writer.addPage(pdf_reader.getPage(page))
        name = pdf.split('.')[0]
        with open(f'{name}_{start}_{end}.pdf', 'wb') as f:
            pdf_writer.write(f)
    except:
        return print('error!')
    # i = PdfFileReader('custom.pdf').getNumPages()
    # print(i)
    print('success!')


if __name__ == '__main__':
    print('1.分割pdf  2.合并pdf')
    option = input()
    if option == '1':
        pdf = input('输入当前文件夹下需要处理的PDF:\n')
        custom_split(pdf)
    elif option == '2':
        pdfs = input('输入需要合并的pdf:')
        pdfs = pdfs.split()
        merge_pdf(pdfs)
    else:
        print('输入错误！')


