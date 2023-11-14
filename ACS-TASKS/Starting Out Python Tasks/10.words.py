#input a sentence from the user
sentence = input("Enter a sentence: ")

#splits the sentence into words using whitespace as the seperator
words = sentence.split()

num_words = len(words)

#outputs the number of words
print("Number of words:", num_words)
