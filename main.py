from collections import Counter
import math
import re

#laplasova korekcija
laplace_correction = 1
with open('bsis_textovi/kultura.txt', 'r') as myfile:
    read_from_file_kultura = re.sub("[^a-z A-Z1-9]", "", myfile.read().replace('\n', '').lower())


with open('bsis_textovi/sport.txt', 'r') as myfile:
    read_from_file_sport = re.sub("[^a-z A-z1-9]", "", myfile.read().replace('\n', '').lower())

with open('bsis_textovi/politika.txt', 'r') as myfile:
    read_from_file_politika = re.sub("[^a-z A-Z1-9]", "", myfile.read().replace('\n', '').lower())

#obrisani su svi karakteri osim a-z, A-Z, 1-9
list_culture = []
list_sport = []
list_politics = []



for text in read_from_file_kultura.split('-----'):
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
    for text in text_dict[key]:
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


#odavde pocinje tek program
klasni_tekstovi = []
for key in text_dict:
    spojen_text_klasa = ""
    for text in text_dict[key]:
        spojen_text_klasa += text + ' '
    klasni_tekstovi.append(spojen_text_klasa)


list_of_occurrences = []
for text in klasni_tekstovi:
    occurence_list = []
    for word in set(splitted_input):
        value = 0
        for rec in text.split():
            if word == rec:
                value += 1
        occurence_list.append(value)
    list_of_occurrences.append(occurence_list)


probabilities = []

counter = 0
for occurence_list in list_of_occurrences:
    prob = klass_probability[counter]
    print (prob)
    for occurence in occurence_list:
        prob *= (occurence + laplace_correction) / (word_count_class[counter] + V)
        print("p(C): " + str(klass_probability[counter]) + " occurence: " + str(occurence) + " word count class: " + str(word_count_class[counter]) + " vocabulary: " + str(V))
    probabilities.append(prob)
    counter += 1
    print("\n")

for number in probabilities:
    print (math.log(number))

index = probabilities.index(max(probabilities)) + 1
if index == 1:
    print ("Program misli da je kultura")
elif index == 2:
    print ("Program misli da je sport u pitanju")
elif index == 3:
    print ("Program misli da je politika u pitanju")