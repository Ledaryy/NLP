import gensim
import spacy
from gensim import corpora, models

documents = [
    "Football club Arsenal defeat local rivals this weekend.",
    "Weekend football frenzy takes over London.",
    "Bank open for take over bids after losing millions.",
    "London football clubs bid to move to Wembley stadium.",
    "Arsenal bid 50 million pounds for striker Kane.",
    "Financial troubles result in loss of millions for bank.",
    "Western bank files for bankruptcy after financial losses.",
    "London football club is taken over by oil millionaire from Russia.",
    "Banking on finances not working for Russia.",
]

nlp = spacy.load("en_core_web_sm")
texts = []
for document in documents:
    text = []
    doc = nlp(document)
    for w in doc:
        if not w.is_stop and not w.is_punct and not w.like_num:
            text.append(w.lemma_)
    texts.append(text)

# print(texts)

dictionary = corpora.Dictionary(texts)
# print(dictionary.token2id)

corpus = [dictionary.doc2bow(text) for text in texts]

# print(corpus)

corpora.MmCorpus.serialize("./tmp/corpus.mm", corpus)

tfidf = models.TfidfModel(corpus)

# for document in tfidf[corpus]:
#     print(document)


bigram = gensim.models.Phrases(texts)
texts = [bigram[line] for line in texts]
print(texts)

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

dictionary.filter_extremes(no_below=20, no_above=0.5)
