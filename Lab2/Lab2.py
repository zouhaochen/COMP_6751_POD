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

print()

# 2. create a dictionary e, to represent a single lexical entry for put.
#    Define keys like headword, part-of-speech, arguments, sense, and example, then assign them suitable values.

e = {'headword': 'A style of boot with a severely pointed toe, fashionable in the 1950s.',
     'part-of-speech': 'Noun',
     'sense': 'type of footwear',
     'example': 'Winklepickers were very popular among mods in the 60s.'}

print(e)

print()

# 3. Using the categories defined in NLTK Ch8 in Tables 3.1, 5.1, and 5.2,
#    write a CFG fragment that deals properly with the following:
#    (a) *Joe put on the log.
#    (b) *Joe put the fish on log.
#    (c) Joe really put the fish on the log.
#    (d) Joe never puts fish on logs.


grammar = nltk.CFG.fromstring("""
  S -> NP VP
  NP -> "Joe"
  VP -> IV | TV NP | DatV NP PP | SV Adj | SV S
  PP -> P NP
  IV -> "barked"
  TV -> "put" | "puts" | "saw"
  DatV -> "gave"
  SV -> "said"
  NP -> "Joe" | Det N | Det N PP
  Det -> "a" | "an" | "the"
  N -> "man" | "fish" | "log"
  P -> "on" | "with"
  """)

a = "Joe put on the log".split()
b = "Joe put the fish on log".split()
c = "Joe really put the fish on the log".split()
d = "Joe never puts fish on logs".split()

rd_parser = nltk.RecursiveDescentParser(grammar)
trees = rd_parser.parse(b)
for tree in trees:
    print(tree)




