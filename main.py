from collections import Counter
from entropy import getListOfEntropies
import math
import re



#laplasova korekcija
laplace_correction = 1


read_from_file_kultura = None
number_of_texts_culture = 0
with open('bsis_textovi/kultura.txt', 'r') as myfile:
    cultureTxt = myfile.read()
    number_of_texts_culture = cultureTxt.count("-----")
    print ("broj tekstova iz kulture " + str(number_of_texts_culture))
    read_from_file_kultura = re.sub("[^a-z A-Z1-9]", "", cultureTxt.replace('\n', '').lower())

sportTxt = None
read_from_file_sport = 0
with open('bsis_textovi/sport.txt', 'r') as myfile:
    sportTxt = myfile.read()
    number_of_texts_sport = sportTxt.count('-----')
    print ("broj tekstova iz sporta " + str(number_of_texts_sport))
    read_from_file_sport = re.sub("[^a-z A-z1-9]", "", sportTxt.replace('\n', '').lower())

number_of_texts_politics = 0

read_from_file_politika = None
with open('bsis_textovi/politika.txt', 'r') as myfile:
    politicsTxt = myfile.read()
    number_of_texts_politics = politicsTxt.count('-----')
    print ("broj tekstova iz politike " + str(number_of_texts_politics))
    read_from_file_politika = re.sub("[^a-z A-Z1-9]", "", politicsTxt.replace('\n', '').lower())

#obrisani su svi karakteri osim a-z, A-Z, 1-9

sum_of_all_texts = number_of_texts_culture + number_of_texts_politics + number_of_texts_sport

sport_probability = number_of_texts_sport / sum_of_all_texts
culture_probability = number_of_texts_culture / sum_of_all_texts
politics_probability = number_of_texts_politics / sum_of_all_texts

corpus = (read_from_file_kultura + read_from_file_sport + read_from_file_politika).split(' ')
list_of_entropies = getListOfEntropies(corpus)
list_of_known_words = sorted(list_of_entropies, key=lambda word: word.entropy, reverse=True)

list_of_all_word_content = []

for x in list_of_known_words:
    list_of_all_word_content.append(x.content)
    print(x.content)


list_culture = []
list_sport = []
list_politics = []


for text in read_from_file_kultura.split('-----'): #sve tekstove iz kulture dodajemo u listu
    list_culture.append(text)


for text in read_from_file_sport.split('-----'):
    list_sport.append(text)


for text in read_from_file_politika.split('-----'):
    list_politics.append(text)


text_dict = {
    'kultura': list_culture,
    'sport': list_sport,
    'politika': list_politics
}


for key in text_dict:
    for text in text_dict[key]: #ispisujemo sve tekstove na konzolu
        print(text)
    print ("\n")


klass_probability = []
number_of_texts = 0
for key in text_dict:
    number_of_texts += len(text_dict[key])


for key in text_dict:
    klass_probability.append(len(text_dict[key]) / number_of_texts)

print("class probabilty: " + str(klass_probability))

number_of_classes = len(text_dict)
print("number of classes: " + str(number_of_classes))

word_count_class = []
for key in text_dict:
    value = 0
    class_text = ""
    for text in text_dict[key]:
        class_text += text + ' '

    counter = Counter(class_text.split())
    print(counter)
    value += sum(counter.values())
    word_count_class.append(value)

#ispisuje koliko reci ima u kojoj klasi
counter = 1
for value in word_count_class:
    print("word count in class: " + str(counter) + ": " + str(value))
    counter += 1

#duzina vokabulara (length dictionary-a u kom se nalaze tekstovi)

def vocabulary_length(corps):
    dictionary = ""
    for key in corps:
        for text in corps[key]:
            dictionary += text + ' '
    temp_dict = Counter(dictionary.split())
    return len(temp_dict)

V = vocabulary_length(text_dict)
print("vocabulary length is: " + str(vocabulary_length(text_dict)))

string_from_input = input("unesi tekst\n")
splitted_input = string_from_input.split()
print(splitted_input) #ispisuje listu unetih reci

occurences_list_culture = []


spojeni_textovi_iz_kulture = ""
for text in text_dict['kultura']:
    spojeni_textovi_iz_kulture += text + ' '

for word in set(splitted_input):
    value = 0
    for rec in spojeni_textovi_iz_kulture.split():
        if word == rec:
            value += 1
    occurences_list_culture.append(value)


print(occurences_list_culture)

probability = klass_probability[0]
for occurence in occurences_list_culture:
    probability *= (occurence + 1) / (word_count_class[0] + V)

print (math.log(probability))


#odavde tek pocinje program
klasni_tekstovi = []
for key in text_dict:
    joined_txts = ""
    for text in text_dict[key]:
        joined_txts += text + ' '
    klasni_tekstovi.append(joined_txts)




#ova lista se popunjava tako sto se racunaju entropije
#known_words = ["reziser", "reditelj", "delo", "slikar", "pisao", "dela", "umetniku", "nedokucivi", "ideal", "pesnik", "pise", "istoricar", "impresionistickom", "umetnosti", "kustosi",
 #              "modeli", "feminizam", "muzeju", "studio", "izlozba", "kosarkas", "utakmicu", "utakmica", "plej-of", "jokic", "bek", "partije", "sutu", "plasman", "cetvrtini", "branioca", "kandidaturu", "kazna",
  ##            "izvesnije", "direktor", "derbi", "izbori", "plati", "kauciju", "talenat", "stranke", "izborni", "glasanje", "birackog", "mesta", "mesto", "stranka",
    #           "proces", "birackih", "materijal", "odsto", "sns", "sps", "srs", "js", "grupa", "gradjana", "takmici", "skupstinu", "skupstina", "lista", "opstina",
     #          "opstine", "politickih", "partija", "tenderima", "kosovo", "ratne", "zlocin", "ratni", "pokret", "partnerstvo", "izborima"]

occured_known_words = []
for word in set(list_of_all_word_content):
    for word1 in set(splitted_input):
        if word == word1:
            occured_known_words.append(word1)

print (occured_known_words)

#list of words moze da bude i set(splitted_input)
list_of_words = occured_known_words


def get_list_of_occurences(list_of_words):
    list_of_occurrences = []
    for text in klasni_tekstovi:
        occurence_list = []
        for word in list_of_words:
            value = 0
            for rec in text.split():
                if word == rec:
                    value += 1
            occurence_list.append(value)
        list_of_occurrences.append(occurence_list)
    return list_of_occurrences


list_of_occurences = get_list_of_occurences(list_of_words)


probabilities = []


counter = 0
for occurrence_list in list_of_occurences:
    prob = klass_probability[counter]
    print (prob)
    for occurence in occurrence_list:
        prob *= (occurence + laplace_correction) / (word_count_class[counter] + V)
        print("p(C): " + str(klass_probability[counter]) + " occurence: " + str(occurence) + " word count class: " + str(word_count_class[counter]) + " vocabulary: " + str(V))
    probabilities.append(prob)
    counter += 1
    print("\n")

print ("KULTURA - SPORT - POLITIKA")
for number in probabilities:
    print (math.log(number))

index = probabilities.index(max(probabilities)) + 1
if index == 1:
    print ("klasa: KULTURA")
elif index == 2:
    print ("klasa: SPORT")
elif index == 3:
    print ("klasa: POLITIKA")