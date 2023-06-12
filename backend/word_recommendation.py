import nltk
from nltk.corpus import wordnet

def get_synonyms_antonyms(word):
    synonyms = []
    antonyms = []

    # Retrieve synsets for the given word
    synsets = wordnet.synsets(word)

    for synset in synsets:
        for lemma in synset.lemmas():
            # Add synonyms
            synonyms.append(lemma.name())
            # Add antonyms if available
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())

    return synonyms, antonyms
if __name__ == "__main__":
    word = input("Enter a word: ")
    synonyms, antonyms = get_synonyms_antonyms(word)
    print("Synonyms:", synonyms)
    print("Antonyms:", antonyms)

