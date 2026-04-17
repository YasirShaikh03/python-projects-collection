import pyttsx3
from pypdf import PdfReader

# use raw string for Windows path
reader = PdfReader(r"A:\for small phython project\Ghosts Book 1 Excerpt.pdf")

# get first page
page = reader.pages[3]

# extract text
text = page.extract_text()

# initialize pyttsx3
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
