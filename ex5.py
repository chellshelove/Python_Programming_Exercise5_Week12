from collections import Counter

# Open the file and read its content
with open("news.txt", "r") as file:
    text = file.read()  # Read the entire content of the file

# Split the text into words and normalize by converting to lowercase
words = text.lower().split()

# Count the frequency of each word
word_counts = Counter(words)

# Sort the dictionary by value (word frequency) in descending order
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Get the top five most frequent words
top_five_words = sorted_word_counts[:5]

# Print the top five words
print("Top 5 most frequent words:")
for word, count in top_five_words:
    print(f"{word}: {count}")