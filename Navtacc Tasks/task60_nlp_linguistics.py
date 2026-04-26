import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
# Linguistics using NLTK
# Download necessary data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "Artificial Intelligence is transforming the financial sector at NetSol."

# Tokenization
tokens = word_tokenize(text)
# Part of Speech (POS) Tagging - Identifying Nouns, Verbs, etc.
pos_tags = nltk.pos_tag(tokens)

print("Tokens:", tokens)
print("\nPOS Tags (Linguistic Analysis):\n", pos_tags)
