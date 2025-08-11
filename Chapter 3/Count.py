def word_count(S, search):
    return S.count(search)

def main():
    S = list(input("Input a sentence: ").split())
    search = input("Input a word to search for: ")
    count = word_count(S, search)
    print("In the sentence, the word '{}' appears {} times.".format(search, count))
    return count

word = main()