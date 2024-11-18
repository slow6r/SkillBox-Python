def can_form_palindrome(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    return odd_count <= 1

string = input("Введите строку: ")
if can_form_palindrome(string):
    print("Можно сделать палиндромом")
else:
    print("Нельзя сделать палиндромом")
