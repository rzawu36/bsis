from math import log
import re


class Word:
    def __init__(self, content, entropy):
        self.content = content
        self.entropy = entropy


culture = None
number_of_texts_culture = 0
with open('bsis_textovi/kultura.txt', 'r') as myfile:
    kulturaTxt = myfile.read()
    number_of_texts_culture = kulturaTxt.count("-----")
    culture = re.sub("[^a-z A-Z1-9]", "", kulturaTxt.replace('\n', '').lower())


sport = None
number_of_texts_sport = 0
with open('bsis_textovi/sport.txt', 'r') as myfile:
    sportTxt = myfile.read()
    number_of_texts_sport = sportTxt.count('-----')
    sport = re.sub("[^a-z A-z1-9]", "", sportTxt.replace('\n', '').lower())

politics = None
number_of_texts_politics = 0
with open('bsis_textovi/politika.txt', 'r') as myfile:
    politikaTxt = myfile.read()
    number_of_texts_politics = politikaTxt.count('-----')
    politics = re.sub("[^a-z A-Z1-9]", "", politikaTxt.replace('\n', '').lower())

sum_of_all_texts = number_of_texts_culture + number_of_texts_politics + number_of_texts_sport

sport_probability = number_of_texts_sport / sum_of_all_texts
culture_probability = number_of_texts_culture / sum_of_all_texts
politics_probability = number_of_texts_politics / sum_of_all_texts

def getHX(sport, politics, culture):
    return -(sport * log(sport, 10) + culture * log(culture, 10) + politics * log(politics, 10))

HX = getHX(sport_probability, politics_probability, culture_probability)


def HXNotInclude(word, allWords):
    politicsCount = politics.count(word)
    sportCount = sport.count(word)
    cultureCount = culture.count(word)
    inPolitics = -(((allWords - politicsCount) / allWords) * log(((allWords - politicsCount) / allWords), 10))
    inSport = -(((allWords - sportCount) / allWords) * log(((allWords - sportCount) / allWords), 10))
    inCulture = -(((allWords - cultureCount) / allWords) * log(((allWords - cultureCount) / allWords), 10))
    return (inPolitics + inSport + inCulture)

def HXInclude(word, allWords):
    politicsCount = politics.count(word) + 1
    sportCount = sport.count(word) + 1
    cultureCount = culture.count(word) + 1
    inPolitics = -((politicsCount / allWords) * log((politicsCount / allWords), 10))
    inSport = -((sportCount / allWords) * log((politicsCount / allWords), 10))
    inCulture = -((cultureCount / allWords) * log((cultureCount / allWords), 10))
    return inCulture + inSport + inPolitics




def getListOfEntropies(corpus):
    list_of_known_words = []
    allWords = len(corpus)
    for word in corpus:
        if word is not "":
            informationalGain = HX - HXInclude(word, allWords) - HXNotInclude(word, len(corpus))
            word = Word(word, informationalGain)
            list_of_known_words.append(word)
    return list_of_known_words



