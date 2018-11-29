from nltk.corpus import wordnet

synonyms = []

for syn in wordnet.synsets("home"):
    for lm in syn.lemmas():
             synonyms.append(lm.name())
print (set(synonyms))