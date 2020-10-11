def hash_function(text):
    encoded = text.encode()
    total = 0
    for c in encoded:
        total += c 
    return total % 8

table = [None] * 10

table[hash_function('parth')] = '3 ayears'

print(table)

print(table[hash_function('parth')])