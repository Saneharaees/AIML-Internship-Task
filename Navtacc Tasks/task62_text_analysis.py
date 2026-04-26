from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# Analyzing text using Vectorization
corpus = [
    'Deep learning is great.',
    'Machine learning is also great.',
    'Python is used for deep learning.'
]

# TF-IDF Analysis (Word Importance)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

print("Feature Names (Words):", vectorizer.get_feature_names_out())
print("\nTF-IDF Matrix Shape:", X.shape)
