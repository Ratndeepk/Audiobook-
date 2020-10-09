#importing important libraries
import pyttsx3
import PyPDF2

#opening pdf using file handling here i'm reading novel named inferno
book = open('inferno.pdf', 'rb')

#reading pdf using PyPDF2 library
pdfReader = PyPDF2.PdfFileReader(book)

#number of pages in book
pages = pdfReader.numPages

#initializing pyttsx3
speaker = pyttsx3.init()

#loop to read every page
for num in range(1,pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()


# :)
