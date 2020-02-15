import mammoth
f = open(r"C:\Users\rishy\Desktop\rr\my_word_file.docx", 'rb')
b = open(r'converted_file.html', 'wb')
document = mammoth.convert_to_html(f)
b.write(document.value.encode('utf8'))
f.close()
b.close()
