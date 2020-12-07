#coding:utf-8

def add (word_fr , word_en , dic):
    if not word_fr in dic :
        dic[word_fr] = word_en

def french_words (dic):
    for word_fr in dic.keys():
        print(word_fr)

def english_words (dic):
    for word_en in dic.values():
        print(word_en)

def delete (character, dic):
    for case in list(dic.keys()):
        if case[0] == character:
            del dic[case]


dic_animals = {"chat":"cat","chien":"dog"}
print("step 1:\n {}".format(dic_animals))

add("souris", "mouse", dic_animals)
print("step 2:\n {}".format(dic_animals))

print ("\nFR words\n") 
french_words(dic_animals)

print ("\nEn words\n") 
english_words(dic_animals)

print ("\nDelete\n") 
delete( "c" , dic_animals )
print (dic_animals)

