# 1. install NLTK3
import nltk


# 2. download the version of the Reuters corpus available in NLTK
# download the reuters corpus
nltk.download('reuters')
# download the english tokenizer
nltk.download('punkt')
from nltk.corpus import reuters


# 3.a. in the Reuters corpus, what are the number of documents?
print(len(reuters.fileids()))


# 3.b. in the Reuters corpus, what are the number of words?
print(len(reuters.words()))


# 3.c. in the Reuters corpus, what are the number of sentences?
print(len(reuters.sents()))


# 4.d. for the text with fileid `training/9920', determine the number of words?
print(len(reuters.words(fileids=['training/9920'])))


# 4.e. for the text with fileid `training/9920', determine the number of single word prepositions?
single_word_prepositions = ['about', 'beside', 'near', 'to', 'above', 'between', 'of', 'towards', 'across', 'beyond', 'off', 'under', 'after', 'by', 'on', 'underneath', 'against', 'despite', 'onto', 'unlike', 'along', 'down', 'opposite', 'until', 'among', 'during', 'out', 'up', 'around', 'except', 'outside', 'upon', 'as', 'for', 'over', 'via', 'at', 'from', 'past', 'with', 'before', 'in', 'round', 'within', 'behind', 'inside', 'since', 'without', 'below', 'into', 'than', 'beneath', 'like', 'through']
count = 0
for w in reuters.words(fileids=['training/9920']):
    # need to consider the lower and upper case
    if w.lower() in single_word_prepositions:
        count += 1
print(count)


# 5. in NLTK, create a table that lists leIDs for each of the 90 categories. Retain a copy of this index.
categories = reuters.categories()
tableList = []
for category in categories:
    tableList.append(reuters.fileids([category]))
print(tableList)


def word_freq(word, fileid) -> int:
    frequency = 0
    words = reuters.words(fileids=[fileid])
    for w in words:
        if w == word:
            frequency += 1
    return frequency

# 6. write a function word_freq() that takes a word and a fileID, and computes the frequency of the word in that file.
print(word_freq('to', 'training/9920'))