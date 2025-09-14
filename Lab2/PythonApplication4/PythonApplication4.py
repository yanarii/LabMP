sentence = input("Введите строку, слова через ';': ")
words = sentence.split(";")  # разделяем по ';'
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Самое длинное слово:", longest_word)

