import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('stopwords')

# Text Pre-processing steps
text = "The students are learning Deep Learning and coding in Python."
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

# 1. Lowercasing & Tokenizing
tokens = nltk.word_tokenize(text.lower())

# 2. Removing Stopwords & Stemming (Root word extraction)
filtered_text = [ps.stem(w) for w in tokens if w not in stop_words and w.isalnum()]

print("Original:", text)
print("After Processing:", filtered_text)
