# word counter
def word_counter(text):
    words = text.split()
    word_count = {}
    
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

text = input("Enter a paragraph of text: ")
word_counts = word_counter(text)

print("Word Counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
