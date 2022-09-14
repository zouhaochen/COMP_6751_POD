# 1. manually assign all possible POS tags for each of the words in the following sentence:
#    They wind back the clock, while we chase after the wind.
#    Use the NLTK Ch5 POS tagset for this exercise.
#    Solution:
#    (This solution is based on the Universal POS tagset: https://universaldependencies.org/u/pos/)
#    (There are also another tagset Penn Treebank: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)
#    They:  PRON    (pronoun)
#    wind:  VERB    (verb)
#    back:  ADP     (adposition)
#    the:   DET     (determiner)
#    clock: NOUN    (noun)
#    ,:     PUNCT   (punctuation)
#    while: CCONJ   (coordinating conjunction)
#    we:    PRON    (pronoun)
#    chase: VERB    (verb)
#    after: ADP     (adposition)
#    the:   DET     (determiner)
#    wind:  NOUN    (noun)
#    .:     PUNCT   (punctuation)

import nltk
from nltk import word_tokenize

sentence = word_tokenize("They wind back the clock, while we chase after the wind.")

# Penn Treebank tagset
print(nltk.pos_tag(sentence))

print()

# Universal tagset
print(nltk.pos_tag(sentence, tagset='universal'))



# 2. create a dictionary e, to represent a single lexical entry for put.
#    Define keys like headword, part-of-speech, arguments, sense, and example, then assign them suitable values.








