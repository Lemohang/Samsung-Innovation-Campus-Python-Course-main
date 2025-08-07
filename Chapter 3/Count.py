def word_count(S, x):
    return S.count(x)

def main():
    S = list(input("Input a sentence: ").split())
    x = input("Input a word to search for: ")
    count = word_count(S, x)
    print("In the sentence, the word '{}' appears {} times.".format(x, count))
    return count

word = main()