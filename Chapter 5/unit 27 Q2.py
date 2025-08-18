def selection_sort(word):
    word_list = list(word.lower())
    for i in range(0, len(word_list) - 1):
        current_min = i
        for j in range(i + 1, len(word_list)):
            if word_list[j] < word_list[current_min]:
                current_min = j
        word_list[i], word_list[current_min] = word_list[current_min], word_list[i]
    return word_list



def insertion_sort(word):
    chars = list(word.lower())
    for i in range(1, len(chars)):
        key = chars[i]
        j = i-1
        while j >= 0 and key < chars[j]:
            chars[j+1] = chars[j]
            j -= 1
        chars[j+1] = key
    return chars

def is_anagram_builtin(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    return sorted(word1) == sorted(word2)

def is_anagram_selection(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    if len(word1) != len(word2):
        return False
    return selection_sort(word1) == selection_sort(word2)

def is_anagram_insertion(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    if len(word1) != len(word2):
        return False
    return insertion_sort(word1) == insertion_sort(word2)

while True:
    print("\nAnagram Checker Menu")
    print("1. Use Python built-in sorted()")
    print("2. Use Selection Sort")
    print("3. Use Insertion Sort")
    print("4. Exit")
    choice = input("Choose a method (1-4): ")

    if choice in ["1", "2", "3"]:
        word1 = input("Enter the first word: ")
        word2 = input("Enter the second word: ")
        if choice == "1":
            result = is_anagram_builtin(word1, word2)
            method = "Python built-in sorted()"
        elif choice == "2":
            result = is_anagram_selection(word1, word2)
            method = "Selection Sort"
        else:
            result = is_anagram_insertion(word1, word2)
            method = "Insertion Sort"
        print(f"Using {method}: Are they anagrams? {result}")
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")