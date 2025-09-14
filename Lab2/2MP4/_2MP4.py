sentence = input("Введите строку: ")
word_to_find = input("Введите слово для поиска: ")

found = False
for word in sentence.split(" "):
    if word == word_to_find:
        found = True
        break

if found:
    print("Слово найдено!")
else:
    print("Слово не найдено.")

