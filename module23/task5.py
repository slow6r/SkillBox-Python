from collections import Counter

def frequency_analysis(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read().lower()

    letters = [char for char in text if char.isalpha()]
    total_letters = len(letters)
    frequencies = Counter(letters)

    with open(output_file, 'w') as file:
        for letter, count in sorted(frequencies.items(), key=lambda x: (-x[1], x[0])):
            file.write(f"{letter} {count / total_letters:.3f}\n")

frequency_analysis('text.txt', 'analysis.txt')
