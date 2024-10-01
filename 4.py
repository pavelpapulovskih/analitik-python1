def count_words(texts):
 return sum(len(text.split()) for text in texts)
# Пример использования
texts = ["Hello world", "Python is great", "I love coding"]
print(count_words(texts)) # Вывод: 8
