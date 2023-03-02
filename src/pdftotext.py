import PyPDF2
from PyPDF2 import PdfReader

def pdftotext():
    reader = PdfReader('PokemonSong.pdf')
    page = reader.pages[0]
    text = page.extract_text()
    return text

