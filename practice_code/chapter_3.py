# import spacy

# nlp = spacy.load('en_core_web_sm')

# doc = nlp(u"This is a sentence.")

# 41
import en_core_web_md

nlp = en_core_web_md.load()

doc = nlp(u"This is a sentence.")

# POS Tagging

doc  = nlp(u"John and I went to the park.")

for token in doc:
    print((token.text, token.pos_))