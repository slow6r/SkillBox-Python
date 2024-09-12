text = input("Введите текст: ")

words = text.split()  
longest_word = max(words, key=len) 

print(f"Самое длинное слово, букв: {len(longest_word)}")
