
import spacy  # importing spacy
nlp = spacy.load('en_core_web_sm') # specifying the model we want to use. Remember to install this model by typing python -m spacy download en_core_web_md into your command line

# Similarity with Spacy
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("lion")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(word4.similarity(word1))

# Working with vectors
tokens = nlp('cat apple monkey banana lion')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Working with sentences
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go", "Hello, there is my car", "I\'ve lost my car in my car", "I\'d like my boat back", "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


'''
1. Similiarites between cat, monkey, banana and my example of lion:

    - All numbers are decimals
    - Number indicates similarity so higher the number the more similar
    - Cat and Monkey are the most similar
    - Banana and Cat are least similar
    - Similarity number is different in some cases to what semantic analysis would show

2.  Difference between running sm instead of md:

    - Warning of no word vectors has been loaded and so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements
    - Similarity is higher and more of what you would expect e.g. in 0.6-08 range between animals and banana 
    - Working with sentences figures did not change between sm and md




'''