import pyttsx3
import PyPDF2
book = open("lora.pdf",'rb')
pdfReader= PyPDF2.PdfFileReader(book)
pages= pdfReader.numPages
print(pages)
speaker= pyttsx3.init()

rate = speaker.getProperty('rate')
print(rate)
speaker.setProperty('rate', 180)

voices = speaker.getProperty('voices')


for i in range(10,pages):
    page=pdfReader.getPage(i)
    text=page.extractText()
    speaker.setProperty('voice', voices[0].id)
    speaker.say(text)
    speaker.runAndWait()