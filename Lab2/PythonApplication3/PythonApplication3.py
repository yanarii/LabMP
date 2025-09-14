sentence = input("Введите строку с пробелами: ")
words = sentence.split(" ")  # делим строку на слова
longest_word = ""  # начальное значение

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Самое длинное слово:", longest_word)

