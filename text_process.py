# import pdftotext
import requests
import PyPDF2
import re
import wikipedia
from config import *


def pdf2_process(_book):
    global p_end
    global page_words

    text = ""
    pdf_file = open(_book, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    # number_of_pages = read_pdf.getNumPages()

    for I in range(p_start, p_end):
        print(I)
        page = read_pdf.getPage(I)
        page_content = page.extractText()
        page_words.append(len(page_content.split(" ")))
        # page_content = page_content.encode('utf-8')

        text += page_content

    return format_text(text)


# def pdf_process(_book):
#     global p_end
#     global page_words

#     text = ""
#     with open(_book, "rb") as f:
#         pdf = pdftotext.PDF(f)

#     for I in range(p_start, p_end):
#         print(I)
#         page = pdf[I]
#         for line in page:
#             text += line
#         page_words.append(len(page.split(" ")))

#     return format_text(text)


def txt_process(_book):
    global p_end
    global page_words

    text = ""
    print(text)
    with open(_book, "rb") as f:
        for line in f:

            text += line

    return format_text(text)


def url_process(_book):
    p = wikipedia.page(_book)
    print(p.content)
    return format_text(p.content)


def format_text(_text):
    # print(_text)
    # spanish accents %[A-Z0-9]{2}

    return re.sub('[^a-zA-Z0-9,\/!?.\'\-\r\n: ]', '', _text).replace('  ', '').replace("-\n\n", '').replace("-\n", '').replace("\n", ' ').replace('  ', ' ').split(" ")
