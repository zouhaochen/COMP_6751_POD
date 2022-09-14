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

grammar1 = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP | V PP | V NP PP | Adv V NP PP
PP -> P NP
NP -> PropN | N | Det N | Det N PP
PropN -> "Joe"
V -> "put" | "puts"
Adv -> "really" | "never"
Det -> "the"
N -> "log" | "fish" | "logs"
P -> "on"
""")

sentenceA = "Joe put on the log".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for treeA in rd_parser.parse(sentenceA):
    print(treeA)
    treeA.draw()

print()

sentenceB = "Joe put the fish on log".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for treeB in rd_parser.parse(sentenceB):
    print(treeB)
    treeB.draw()


print()

sentenceC = "Joe really put the fish on the log".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for treeC in rd_parser.parse(sentenceC):
    print(treeC)
    treeC.draw()

print()

sentenceD = "Joe never puts fish on logs".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for treeD in rd_parser.parse(sentenceD):
    print(treeD)
    treeD.draw()
