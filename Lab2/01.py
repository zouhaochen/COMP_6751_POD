import nltk

pattern = r'''(?x) # set flag to allow verbose regexps
(?:[a-zA-Z]\.)+ # abbreviations, e.g. U.S.A.
| \w+(?:-\w+)* # words with optional internal hyphens
| \$?\d+(?:\.\d+)?%? # currency and percentages, e.g. $12.40, 82%
| \.\.\. # ellipsis
| [][.,;"'?():-_`] # these are separate tokens
'''

print(nltk.regexp_tokenize("The U.S.A.  e.g. is a country.",pattern))
