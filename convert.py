from gtts import gTTS
import os
import PyPDF2


def speak(a):
    tts = gTTS(text=a, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
    

path = open('file.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(path)

from_page = pdfReader.getPage(10)
  
# extracting the text from the PDF
text = from_page.extractText()

print (text)
speak(text)
