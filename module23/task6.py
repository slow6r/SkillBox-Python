from collections import Counter
import zipfile

def analyze_war_and_peace(zip_path, text_file):
    # Распаковка архива
    with zipfile.ZipFile(zip_path, 'r') as archive:
        archive.extractall()
    
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    frequencies = Counter(text)
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: -x[1])
    
    for char, count in sorted_frequencies:
        if char.isalpha():
            print(f"{char}: {count}")

analyze_war_and_peace('voina-i-mir.zip', 'voina-i-mir.txt')
