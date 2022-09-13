# 1. install NLTK3
import nltk


# 2. download the version of the Reuters corpus available in NLTK
# download the reuters corpus
nltk.download('reuters')
# download the english tokenizer
nltk.download('punkt')
from nltk.corpus import reuters


# 3.a in the Reuters corpus, what are the number of documents?
print(len(reuters.fileids()))
# 3.b in the Reuters corpus, what are the number of words?
print(len(reuters.words()))


