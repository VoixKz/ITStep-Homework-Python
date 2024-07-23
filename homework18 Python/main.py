#python -m venv venv
#venv\Scripts\activate
#pip install python-docx

from docx import Document
user_input = input("Введите текст для сохранения в Word-файл: ")
doc = Document()
doc.add_paragraph(user_input)
doc.save('homework18 Python/input.docx')
print("Файл 'input.docx' успешно сохранён")

#pip install auto-py-to-exe
#auto-py-to-exe