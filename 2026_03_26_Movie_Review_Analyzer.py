reviews = [
    "This movie is amazing",
    "The film was terrible",
    "I love the story",
    "Worst acting ever",
    "Great direction and music"
]

positive = ["amazing","love","great"]
negative = ["terrible","worst"]

for r in reviews:
    if any(p in r.lower() for p in positive):
        print(r,"-> Positive")
    elif any(n in r.lower() for n in negative):
        print(r,"-> Negative")
    else:
        print(r,"-> Neutral")