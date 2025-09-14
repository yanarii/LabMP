sentence = input("Введите строку: ")
delimiter = input("Введите символ-разделитель: ")
words = sentence.split(delimiter)

shortest_word = words[0]  # начинаем с первого слова
for word in words:
    if len(word) < len(shortest_word):
        shortest_word = word

print("Самое короткое слово:", shortest_word)
