import spacy

nlp = spacy.load("en_core_web_md")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# interesting, how spacy determines the level of similarity of one set over the other(i.e. can and monkey vs monkey and banana)
# monkey and banana are similar, probably because monkeys eat bananas. A mich less similarity found between cat and banana.

word1 = nlp("road")
word2 = nlp("plane")
word3 = nlp("passenger")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# in example.py # the similarity is less when using sm model. it works with the warning sentence explaining that the similarity method may not be useful

