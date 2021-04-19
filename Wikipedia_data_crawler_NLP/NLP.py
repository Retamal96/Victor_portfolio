import nltk
import spacy
from spacy import displacy

sentence = 'Therefore, administration of PROTELOS and such products should be separated by at least two hours'
tokens = nltk.word_tokenize(sentence)
posTag = nltk.pos_tag(tokens)
print('Part of speech', posTag)


nlp = spacy.load('en_core_web_sm')

doc = nlp(sentence)

for entity in doc.ents:
    print(entity.text, entity.label_)

    displacy.render(doc, style='ent')