from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "AI is transforming healthcare",
    "Machine learning improves predictions",
    "Data science uses statistics and AI",
    "AI helps in automation",
    "Machine learning is part of AI"
]

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(docs)

words = vectorizer.get_feature_names_out()
scores = tfidf.sum(axis=0).A1

for w, s in sorted(zip(words, scores), key=lambda x: x[1], reverse=True)[:5]:
    print(w, round(s,2))