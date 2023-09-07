#input a sentence from the user
sentence = input("Enter a sentence: ")

#splits the sentence into words using whitespace as the seperator
words = sentence.split()

#counts the number of words
num_words = len(words)

#outputs the number of words
print("Number of words:", num_words)
