text = input("Введите текст: ")
text = text.split()
text_new = []
for i in range(len(text)):
    if "абв" not in text[i]:
        text_new.append(text[i])
print(type(" ".join(text_new)))
