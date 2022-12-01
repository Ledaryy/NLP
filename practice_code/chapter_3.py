# import spacy

# nlp = spacy.load('en_core_web_sm')

# doc = nlp(u"This is a sentence.")

# 41
import en_core_web_md

nlp = en_core_web_md.load()

doc = nlp("This is a sentence.")

# POS Tagging

doc = nlp("John and I went to the park.")

# for token in doc:
#     print((token.text, token.pos_))

# NER 47
doc = nlp("Microsoft has offices all over the Europe.")

# for ent in doc.ents:
#     print((ent.text, ent.label_))

# STOP WORDS 49


from spacy.lang.en.stop_words import STOP_WORDS

STOP_WORDS.add("btw")

# Lemmatization 50
STOP_WORDS.add("field")
doc = nlp("the horse galloped down the field and past the river.")
sentence = []
for w in doc:
    if w.text != "n" and not w.is_stop and not w.is_punct and not w.like_num:
        sentence.append(w.lemma_)
print(sentence)
