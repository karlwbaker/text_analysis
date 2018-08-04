#!/usr/bin/env python3

import nltk
from collections import Counter

MALE = 'male'
FEMALE = 'female'
UNKNOWN = 'unknown'
BOTH = 'both'

MALE_WORDS = []
#    "men's",'men','him',"he's",'his',
#    'boy','boys','brother','brothers','father','fathers','fiance',
#    'god','grandfather','grandson','groom','he','himself',
#    'husband','husbands','king','male','man','nephew','nephews',
#    'priest','prince','son','sons','uncle','uncles','widower',
#    'widowers',
#    'soldier','general','commander'
#]

print(len(MALE_WORDS))

PATH = r'C:\Users\karls\Anaconda2\code_projects\text_analysis\corpora\corpora_helper_files'
filename = r'\Men_in_Bible_named.txt'

#with open(PATH+filename) as f:
#    MALE_NAMES = f.readlines() 

#MALE_WORDS_NAMES = set(MALE_WORDS + list(MALE_NAMES))
      
print(len(MALE_WORDS))

FEMALE_WORDS = []
#    "women's",'women',
#    "she's",'her','aunt','aunts','bride','daughter','daughters','female',
#    'fiancee','girl','girls','goddess',
#    'granddaughter','grandmother','herself','ladies','lady',
#    'mother','mothers','niece','nieces',
#    'priestess','princess','queen','she','sister','sisters',
#    'widow','widows','wife','wives','woman',
#    'prostitute','betrothed','concubine'
#]
      
print(len(FEMALE_WORDS))

filename = r'\Women_in_Bible_named.txt'

#with open(PATH+filename) as f:
#    FEMALE_NAMES = f.readlines() 

#FEMALE_WORDS_NAMES = set(FEMALE_WORDS + list(FEMALE_NAMES))

print(len(FEMALE_WORDS))

      
      
def genderize(words):

    mwlen = len(MALE_WORDS.intersection(words))
    fwlen = len(FEMALE_WORDS.intersection(words))

    if mwlen > 0 and fwlen == 0:
        return MALE
    elif mwlen == 0 and fwlen > 0:
        return FEMALE
    elif mwlen > 0 and fwlen > 0:
        return BOTH
    else:
        return UNKNOWN


def count_gender(sentences):

    sents = Counter()
    words = Counter()

    for sentence in sentences:
        gender = genderize(sentence)
        sents[gender] += 1
        words[gender] += len(sentence)

    return sents, words


def parse_gender(text):

    sentences = [
        [word.lower() for word in nltk.word_tokenize(sentence)]
        for sentence in nltk.sent_tokenize(text)
    ]

    sents, words = count_gender(sentences)
    total = sum(words.values())

    for gender, count in words.items():
        pcent = (count / total) * 100
        nsents = sents[gender]

        print(
            "{:0.3f}% {} ({} sentences)".format(pcent, gender, nsents)
        )

if __name__ == '__main__':
    with open('ballet.txt', 'r') as f:
        parse_gender(f.read())
