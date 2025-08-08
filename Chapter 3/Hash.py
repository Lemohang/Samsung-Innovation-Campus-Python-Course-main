class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None for i in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        hash = self.hash_function(key)
        self.hash_table[hash] = (key, value)

    def __getitem__(self, key):
        hash = self.hash_function(key)
        return self.hash_table[hash]


roman_numerals = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

def int_to_roman(num):
    result = ""
    for value in sorted(roman_numerals.keys(), reverse=True):
        while num >= value:
            result += roman_numerals[value]
            num -= value
    return result

size = 10
converter = HashTable(size)

num = int(input("Enter a number: "))
print(int_to_roman(num))
    
    
