def build_synonyms(n):
    synonyms = {}
    for i in range(1, n + 1):
        pair = input(f"{i}-я пара: ").split(" — ")
        synonyms[pair[0].lower()] = pair[1]
        synonyms[pair[1].lower()] = pair[0]
    return synonyms

def find_synonym(synonyms):
    while True:
        word = input("Введите слово: ").lower()
        if word in synonyms:
            print(f"Синоним: {synonyms[word]}")
            break
        else:
            print("Такого слова в словаре нет.")

n = int(input("Введите количество пар слов: "))
synonyms = build_synonyms(n)
find_synonym(synonyms)
