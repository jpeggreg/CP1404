# program to count the occurrences of words in a string. It asks the user for a string,
# then print the counts of how many of each word are in the file


word_count = {}
user_text = input("Text: ").lower()
#TEXT = "this is a collection of words of nice words this is a fun thing it is"
words = user_text.split()
for word in words:
    counter = word_count.get(word, 0)
    word_count[word] = counter + 1
words = list(word_count.keys())
words.sort()
max_length = max(len(word) for word in words)
for word in words:
    print("{:{}} : {}".format(word, max_length, word_count[word]))





