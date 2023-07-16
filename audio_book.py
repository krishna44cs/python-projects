import pyttsx3
import PyPDF2
book = open('lab.pdf','rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)
print(pages)
speaker =pyttsx3.init()
for num in range(7,pages):
    page = pdfReader.pages[7]
    text = page.extract_text()
    speaker.say(text)
    speaker.say("hey Good Morning,lets read a book")
    speaker.runAndWait()